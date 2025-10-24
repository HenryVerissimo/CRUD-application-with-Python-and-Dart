from fastapi import FastAPI
from fastapi.testclient import TestClient


from src.dependencies.controllers import get_user_controller
from tests.mocks.user_controller_mock import MockingSuccessfulResponses


def test_what_the_create_users_route_returns(
    get_client: TestClient, get_app: FastAPI
) -> None:
    get_app.dependency_overrides[get_user_controller] = MockingSuccessfulResponses

    payload = {
        "username": "TestUser",
        "email": "TestUser@gmail.com",
        "password": "TestUserPassword123@",
        "confirm_password": "TestUserPassword123@",
    }

    expected_response = {"id": 1, "username": "TestUser", "email": "TestUser@gmail.com"}

    response = get_client.post(url="/users/", json=payload)

    assert response.status_code == 201
    assert response.json() == expected_response
