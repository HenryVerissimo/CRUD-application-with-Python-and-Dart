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


def test_what_the_get_users_route_returns(
    get_client: TestClient, get_app: FastAPI
) -> None:
    get_app.dependency_overrides[get_user_controller] = MockingSuccessfulResponses
    expected_response = [
        {"id": 1, "username": "UserTest1@", "email": "usertest1@gmail.com"},
        {"id": 2, "username": "UserTest2@", "email": "usertest2@gmail.com"},
        {"id": 3, "username": "UserTest3@", "email": "usertest3@gmail.com"},
    ]

    response = get_client.get("/users/")

    assert response.status_code == 200
    assert response.json() == expected_response


def test_what_the_update_users_route_returns(
    get_client: TestClient, get_app: FastAPI
) -> None:
    get_app.dependency_overrides[get_user_controller] = MockingSuccessfulResponses
    payload = {"username": "UpdatedTestName", "email": "updatedtest@gmail.com"}
    expected_response = {
        "id": 1,
        "username": "UpdatedTestName",
        "email": "updatedtest@gmail.com",
    }

    response = get_client.patch("/users/update/1", json=payload)

    assert response.status_code == 200
    assert response.json() == expected_response


def test_what_the_delete_users_route_returns(
    get_client: TestClient, get_app: FastAPI
) -> None:
    get_app.dependency_overrides[get_user_controller] = MockingSuccessfulResponses

    response = get_client.delete("/users/delete/1")

    assert response.status_code == 204
