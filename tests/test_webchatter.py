#!/usr/bin/env python

"""Tests for `webchatter` package."""

import pytest
from webchatter import WebChat, Node
import webchatter
from pprint import pprint

def test_askchat():
    chat = WebChat()
    # initialize the chat
    chat.ask("It is nice today, ahhh")
    chatmap = chat.mapping_by_id()
    assert chat.mapping == chatmap
    # continue chat
    chat.ask("Tell me a joke about the weather.")
    chatmap = chat.mapping_by_id()
    assert chat.mapping == chatmap
    # test chatlog
    chat_log = chat.chat_log
    assert len(chat_log) == 4
    assert chat_log[0] == "It is nice today, ahhh"
    assert chat_log[2] == "Tell me a joke about the weather."
    newchat = WebChat(chat_id=chat.chat_id, node_id=chat.node_id)
    assert newchat.chat_log == chat_log
    # test store
    chat.save("joke.json")
    chat.save("joke-with-id.json", chat_log_only=False)

def test_envs():
    """Test the environment variables."""
    assert webchatter.access_token is not None
    assert webchatter.base_url is not None
    assert webchatter.backend_url is not None

def test_chat_status():
    """Test create chat."""
    chat = WebChat()
    pprint(chat.account_status())
    pprint(chat.beta_features())
    assert len(chat.valid_models()) > 0

def test_chat_list():
    """Test chat list."""
    chat = WebChat()
    pprint(chat.chat_list(limit=3))
    pprint(chat.num_of_chats())