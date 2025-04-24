import os

import gradio as gr
import httpx
from pydantic_ai.messages import ModelMessage, ModelMessagesTypeAdapter

CURRENT_SERVER_LOCATION = os.environ.get("CURRENT_SERVER_LOCATION", "http://localhost:8891")


def load_messages(messages: str) -> list[ModelMessage]:
    if messages.startswith("file://"):
        with open(messages[7:]) as f:
            messages = f.read()
    if messages.startswith("http://") or messages.startswith("https://"):
        response = httpx.get(messages)
        messages = response.text
    return ModelMessagesTypeAdapter.validate_json(messages)


def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity)


app = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],
    outputs=["text"],
)
