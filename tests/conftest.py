import pytest
from fastapi.testclient import TestClient

from pydantic_ai_visual.app import app as APP


@pytest.fixture
async def app():
    yield APP


@pytest.fixture
def client(app):
    with TestClient(
        app,
    ) as client:
        yield client
