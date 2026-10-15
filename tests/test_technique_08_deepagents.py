"""Smoke test for technique 08: KnowledgeGraphMemory over deepagents.

Runs the notebook's triple-store, extractor parsing, and chat orchestration
against fakes, so it needs no API key.
"""
import json
import pathlib

import networkx as nx
import pytest
from deepagents import create_deep_agent
from langchain_core.language_models.fake_chat_models import GenericFakeChatModel
from langchain_core.messages import AIMessage

NB_PATH = (
    pathlib.Path(__file__).parent.parent
    / "all_techniques"
    / "08_knowledge_graph_memory"
    / "knowledge_graph_memory.ipynb"
)


class FakeToolModel(GenericFakeChatModel):
    """deepagents always binds tools; the fake model accepts them as no-op."""

    def bind_tools(self, tools, **kwargs):
        return self.bind(**kwargs)


def _cell(index: int) -> str:
    nb = json.loads(NB_PATH.read_text())
    src = nb["cells"][index]["source"]
    return src if isinstance(src, str) else "".join(src)


@pytest.fixture(scope="module")
def ns():
    """Exec the notebook's implementation cells in one namespace."""
    namespace = {}
    for i in (5, 7, 9, 11, 13, 15, 17, 19, 21):
        exec(_cell(i), namespace)  # noqa: S102 - test code
    return namespace


def test_triple_store_graph_ops(ns):
    TripleStore = ns["TripleStore"]
    store = TripleStore()
    store.add_triple("Priya", "works_at", "Spotify")
    store.add_triple("Priya", "works_at", "Spotify")  # 去重
    store.add_triple("Spotify", "located_in", "Stockholm")

    assert len(store) == 2
    assert ("Priya", "works_at", "Spotify") in store.get_triples()
    assert "Spotify" in store.find_mentioned("I love Spotify apps!")
    assert store.find_path("Priya", "Stockholm") is not None


def test_extractor_parses_tool_calls(ns, monkeypatch):
    TripleExtractor = ns["TripleExtractor"]

    fake_response = AIMessage(
        content="",
        tool_calls=[{
            "name": "store_triples",
            "args": {"triples": [
                {"subject": "Priya", "predicate": "works_at", "object": "Spotify"},
            ]},
            "id": "call_1",
            "type": "tool_call",
        }],
    )

    class StubModel:
        def bind_tools(self, tools, **kwargs):
            assert kwargs.get("tool_choice") == "required"
            return self

        def invoke(self, messages):
            return fake_response

    extractor = TripleExtractor(model=StubModel())
    triples = extractor.extract("I work at Spotify.", "Great to know!")
    assert triples == [{"subject": "Priya", "predicate": "works_at", "object": "Spotify"}]


def test_chat_updates_graph_and_messages(ns, monkeypatch):
    KnowledgeGraphMemory = ns["KnowledgeGraphMemory"]
    TripleStore = ns["TripleStore"]

    model = FakeToolModel(messages=iter(["Noted, Priya.", "Got it."]))

    memory = KnowledgeGraphMemory(model=model, system_prompt="You are concise.")

    # 打桩抽取器：不走真实 API，直接返回固定三元组
    class StubExtractor:
        def extract(self, user_msg, assistant_msg):
            return [{"subject": "Priya", "predicate": "works_at", "object": "Spotify"}]

    memory.extractor = StubExtractor()

    memory.chat("Hi! I'm Priya, I work at Spotify.")
    memory.chat("What do I do for work?")

    assert ("Priya", "works_at", "Spotify") in memory.store.get_triples()
    assert len(memory.messages) == 4
    roles = [m["role"] for m in memory.messages]
    assert roles == ["user", "assistant", "user", "assistant"]


def test_save_load_round_trip(ns, tmp_path):
    TripleStore = ns["TripleStore"]
    store = TripleStore()
    store.add_triple("Alice", "manages", "Bob")

    path = tmp_path / "kg.json"
    store.save(str(path))
    loaded = TripleStore.load(str(path))

    assert loaded.get_triples() == store.get_triples()
    assert loaded.graph.number_of_nodes() == 2
