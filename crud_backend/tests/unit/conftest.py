import pytest

from fastapi import FastAPI
from main import create_app
from fastapi.testclient import TestClient


@pytest.fixture
def get_app() -> FastAPI:
    app = create_app()
    return app


@pytest.fixture
def get_client(get_app: FastAPI) -> TestClient:
    client = TestClient(get_app)
    return client
