import pytest

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
