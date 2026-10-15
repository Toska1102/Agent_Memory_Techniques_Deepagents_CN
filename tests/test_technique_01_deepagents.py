"""Smoke test for technique 01: ConversationBufferMemory over deepagents.

Runs the notebook's buffer logic against a fake chat model, so it needs no
API key. Covers: full-history resend, role alternation, usage fallback,
and JSON persistence round-trip.
"""
import ast
import json
import pathlib

import pytest
from deepagents import create_deep_agent
from langchain_core.language_models.fake_chat_models import GenericFakeChatModel

NB_PATH = (
    pathlib.Path(__file__).parent.parent
    / "all_techniques"
    / "01_conversation_buffer_memory"
    / "conversation_buffer_memory.ipynb"
)


class FakeToolModel(GenericFakeChatModel):
    """deepagents always binds tools; the fake model accepts them as no-op."""

    def bind_tools(self, tools, **kwargs):
        return self.bind(**kwargs)


def _notebook_cell_source(index: int) -> str:
    nb = json.loads(NB_PATH.read_text())
    src = nb["cells"][index]["source"]
    return src if isinstance(src, str) else "".join(src)


def _build_memory_class():
    """Exec the notebook's setup cell and class cell in one namespace."""
    namespace = {}
    exec(_notebook_cell_source(6), namespace)  # noqa: S102 - test code
    exec(_notebook_cell_source(8), namespace)  # noqa: S102 - test code
    return namespace


@pytest.fixture()
def memory_cls(monkeypatch):
    # 打桩：CI 环境没有真实 key 也能构建 ChatOpenAI（不发请求）
    monkeypatch.setenv("LLM_API_KEY", "test-key")
    monkeypatch.delenv("LLM_BASE_URL", raising=False)
    ns = _build_memory_class()
    return ns["ConversationBufferMemory"], ns["to_text"]


def test_buffer_round_trip(memory_cls):
    ConversationBufferMemory, to_text = memory_cls
    model = FakeToolModel(messages=iter(["I will remember that.", "Your name is Alice."]))
    memory = ConversationBufferMemory(model=model, system_prompt="You are concise.")

    assert len(memory) == 0
    first = memory.chat("Hi, I'm Alice.")
    second = memory.chat("What is my name?")

    assert first == "I will remember that."
    assert second == "Your name is Alice."
    assert len(memory) == 4  # user/assistant x2
    roles = [m["role"] for m in memory.get_history()]
    assert roles == ["user", "assistant", "user", "assistant"]
    # usage_metadata 缺失时回退到 tiktoken 估算，记录不能为 0
    assert memory.turn_token_usage[0]["input_tokens"] > 0


def test_history_is_resent_in_full(memory_cls, monkeypatch):
    """chat 每次都必须把完整缓冲区传给 invoke。"""
    ConversationBufferMemory, _ = memory_cls
    seen = []
    model = FakeToolModel(messages=iter(["ok", "ok", "ok"]))

    real_invoke = create_deep_agent(model=model, system_prompt="x").invoke

    def spy_invoke(state, **kwargs):
        seen.append(len(state["messages"]))
        return real_invoke(state, **kwargs)

    memory = ConversationBufferMemory(model=model, system_prompt="x")
    monkeypatch.setattr(memory.agent, "invoke", spy_invoke)

    memory.chat("a")
    memory.chat("b")
    memory.chat("c")
    assert seen == [1, 3, 5], "每轮都应重发全部历史（1, 3, 5 条）"


def test_json_persistence_round_trip(memory_cls, tmp_path):
    ConversationBufferMemory, _ = memory_cls
    model = FakeToolModel(messages=iter(["noted.", "still noted."]))
    memory = ConversationBufferMemory(model=model, system_prompt="x")
    memory.chat("remember 42")

    path = tmp_path / "conversation.json"
    path.write_text(json.dumps(memory.get_history(), ensure_ascii=False))

    restored = ConversationBufferMemory(model=model, system_prompt="x")
    restored.messages = json.loads(path.read_text())
    assert len(restored) == 2
    assert restored.get_history() == memory.get_history()
