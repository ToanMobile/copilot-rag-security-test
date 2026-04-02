"""Tests for the main application."""
from src.app import get_status

def test_status():
    result = get_status()
    assert result["status"] == "ok"
    assert "version" in result
