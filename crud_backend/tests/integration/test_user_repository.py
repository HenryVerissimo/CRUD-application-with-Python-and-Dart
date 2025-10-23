import pytest

from src.schemas.user_schemas import CreateUserSchema, UserUpdate
from src.repositories.user_repository import UserRepository


@pytest.mark.integration
@pytest.mark.db_integration_test
def test_select_user_by_email(repository: UserRepository, create_test_user) -> None:
    user = repository.select_user_by_email("TestUser@gmail.com")

    if user is not None:
        user_data = {"username": user.username, "email": user.email}
        expected = {"username": "TestUser", "email": "TestUser@gmail.com"}

        assert expected == user_data

    else:
        pytest.fail(
            "the test failed because the test user was not found in the database"
        )


@pytest.mark.integration
@pytest.mark.db_integration_test
def test_select_user_by_id(repository: UserRepository, create_test_user) -> None:
    user = repository.select_user_by_id(1)

    if user is not None:
        user_data = {"username": user.username, "email": user.email}
        expected = {"username": "TestUser", "email": "TestUser@gmail.com"}

        assert expected == user_data

    else:
        pytest.fail(
            "the test failed because the test user was not found in the database"
        )


@pytest.mark.integration
@pytest.mark.db_integration_test
def test_select_all_users_in_database(repository) -> None:
    for user in range(1, 4):
        user_schema = CreateUserSchema(
            username=f"Test{user}",
            email=f"Test{user}@gmail.com",
            password=f"TestPassword{user}@",
            confirm_password=f"TesrPassword{user}@",
        )

        repository.create_user(user_schema)

    users = repository.select_users()

    if len(users) >= 3:
        users = [
            {"username": users[0].username, "email": users[0].email},
            {"username": users[1].username, "email": users[1].email},
            {"username": users[2].username, "email": users[2].email},
        ]

        assert users == [
            {"username": "Test1", "email": "Test1@gmail.com"},
            {"username": "Test2", "email": "Test2@gmail.com"},
            {"username": "Test3", "email": "Test3@gmail.com"},
        ]

    else:
        pytest.fail(
            "the test failed because the three test users were not found in the database"
        )


def test_user_update_in_the_database(
    repository: UserRepository, create_test_user
) -> None:
    user_data = UserUpdate(username="UpdatedUser", email="UpdatedUser@gmail.com")

    repository.update_user(1, user_data)

    user = repository.select_user_by_id(1)

    if user is not None:
        assert user.username == "UpdatedUser"
        assert user.email == "UpdatedUser@gmail.com"

    else:
        pytest.fail(
            "the test failed because the test user was not found in the database"
        )


def test_delete_user_in_database(repository: UserRepository, create_test_user) -> None:
    repository.delete_user(1)
    user = repository.select_user_by_id(1)

    assert user is None
