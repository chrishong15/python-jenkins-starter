# tests/test_hello.py
from __future__ import annotations

import builtins
import pytest

from app.hello import hello, run_interactive_loop  # noqa: F401  (ok if you’ve added it)


def test_hello_returns_string() -> None:
    assert hello("Chris") == "Hello, Chris!"


def test_main_loop_greets_until_q(monkeypatch: pytest.MonkeyPatch) -> None:
    # Simulate one name then quit
    inputs: list[str] = ["Chris", "q"]
    monkeypatch.setattr(builtins, "input", lambda _prompt: inputs.pop(0))

    outputs: list[str] = []
    monkeypatch.setattr("builtins.print", outputs.append)

    run_interactive_loop()

    assert outputs == ["Hello, Chris!"]
