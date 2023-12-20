
from webchatter import WebChat, Node, process_messages
from random import randint

def test_process_msgs():
    msgs = [f"find the result of {randint(3, 100)} + {randint(4, 100)}" for _ in range(4)]
    process_messages(msgs[:2], "test.jsonl")
    process_messages(msgs, "test.jsonl")