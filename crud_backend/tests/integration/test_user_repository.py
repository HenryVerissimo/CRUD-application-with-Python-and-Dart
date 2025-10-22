import pytest

from src.schemas.user_schemas import UserUpdate
from src.repositories.user_repository import UserRepository


@pytest.mark.integration
@pytest.mark.db_integration_test
def test_create_and_validate_user_fields(
    repository: UserRepository, create_test_user
) -> None:
    user = repository.select_user_by_email("TestUser@gmail.com")

    if user is not None:
        expected = {"username": user.username, "email": user.email}

        assert expected == {"username": "TestUser", "email": "TestUser@gmail.com"}

    else:
        pytest.fail(
            "the test failed because the test user was not found in the database"
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
