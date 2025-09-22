# tests/test_hello.py
import sys
import importlib
import runpy

from app.hello import hello


def test_hello_returns_expected_string():
    assert hello("World") == "Hello, World!"


def test_main_loop_greets_until_q(monkeypatch, capsys):
    """
    Simulate a user typing 'Chris' then 'q', ensuring we run a fresh copy of app.hello.
    """
    # Remove app.hello from sys.modules to force a clean import
    sys.modules.pop("app.hello", None)

    inputs = iter(["Chris", "q"])

    def fake_input(_prompt=""):
        return next(inputs, "q")

    monkeypatch.setattr("builtins.input", fake_input)

    # Reload app to clear state, then run as __main__
    importlib.invalidate_caches()
    runpy.run_module("app.hello", run_name="__main__")

    out = capsys.readouterr().out.splitlines()
    assert "Hello, Chris!" in out
    assert out.count("Hello, Chris!") == 1