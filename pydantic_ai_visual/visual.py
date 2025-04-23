import httpx
from pydantic_ai.messages import ModelMessage, ModelMessagesTypeAdapter


def load_messages(messages: str) -> list[ModelMessage]:
    if messages.startswith("file://"):
        with open(messages[7:]) as f:
            messages = f.read()
    if messages.startswith("http://") or messages.startswith("https://"):
        response = httpx.get(messages)
        messages = response.text
    return ModelMessagesTypeAdapter.validate_python(messages)
