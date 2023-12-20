# WebChatter

[English](README-EN.md) | [简体中文](README.md)

[![PyPI version](https://img.shields.io/pypi/v/webchatter.svg)](https://pypi.python.org/pypi/webchatter)
[![Tests](https://github.com/cubenlp/webchatter/actions/workflows/test.yml/badge.svg)](https://github.com/cubenlp/webchatter/actions/workflows/test.yml/)
[![Documentation Status](https://img.shields.io/badge/docs-github_pages-blue.svg)](https://apicall.wzhecnu.cn)
[![Coverage](https://codecov.io/gh/cubenlp/webchatter/branch/main/graph/badge.svg)](https://codecov.io/gh/cubenlp/webchatter)

## Features

A Chat encapsulation based on AccessToken, useful for data annotation.

## Installation

```bash
pip install webchatter --upgrade
```

Set environment variables:
```bash
export OPENAI_ACCESS_TOKEN="your_access_token"
export API_REVERSE_PROXY="http://your_reverse_proxy"
export WEB_REVERSE_PROXY="http://your_reverse_proxy/backend-api"
```

Where `OPENAI_ACCESS_TOKEN` can be obtained after logging in to the website [/api/auth/session](https://chat.openai.com/api/auth/session). For reverse proxy setup, you can refer to the [ninja project](https://github.com/gngpp/ninja/).

## Basic Usage

Data annotation example, performing addition:
```py
from webchatter import process_messages
from random import randint

msgs = [f"find the result of {randint(3, 100)} + {randint(4, 100)}" for _ in range(4)]
# Annotate some data and get interrupted
process_messages(msgs[:2], "test.jsonl")
# Continue annotation
process_messages(msgs, "test.jsonl")
```

General usage:

```py
from webchatter import WebChat

# Create a conversation
chat = WebChat()
# Input a question | Return an answer
chat.ask("hello world!")
# Get conversation history
chat.print_log()
```

Other usage:

```py
from webchatter import WebChat
from pprint import pprint
chat = WebChat()

# View the total number of web chats
pprint(chat.num_of_chats())
# Get recent chats
pprint(chat.chat_list(limit=3))
# Continue a specific chat
chat_id = "xxx" # Retrieved from above
newchat = chat.chat_by_id(chat_id)
newchat.ask("ok, let's continue")
```