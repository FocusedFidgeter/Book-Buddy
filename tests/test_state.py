import os
import sys
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from book_buddy.state import State
from unittest.mock import MagicMock

def test_state_initialization():
    """Test the initial state of the State class"""
    state = State()
    assert state.query == ""
    assert state.response == ""
    assert state.is_gen == False
    assert state.sidebar_visible == False
    assert state.current_conversation_id is None
    assert state.selected_provider == "openai"
    assert isinstance(state.available_providers, list)
    assert isinstance(state.available_models, list)
    assert isinstance(state.chat_history, list)

def test_set_query():
    """Test setting the query"""
    state = State()
    test_query = "test query"
    state.set_query(test_query)
    assert state.query == test_query

def test_set_provider():
    """Test changing the provider"""
    state = State()
    new_provider = "cerebras"  # using a valid provider from config
    state.set_provider(new_provider)
    assert state.selected_provider == new_provider
    assert isinstance(state.available_models, list)
    assert state.selected_model == state.available_models[0]

def test_refresh():
    """Test the refresh method"""
    state = State()
    # Set some initial values
    state.query = "test query"
    state.response = "test response"
    state.is_gen = True
    state.chat_history = [("user", "test message")]
    
    # Call refresh
    state.refresh()
    
    # Verify everything is reset
    assert state.query == ""
    assert state.response == ""
    assert state.is_gen == False
    assert state.chat_history == []
    assert state.selected_provider == "openai"
    assert isinstance(state.available_models, list)
    assert state.current_conversation_id is not None  # Should have a new conversation ID
