import pytest

from pytest import FixtureDef

from src.schemas.user_schemas import CreateUserSchema


@pytest.mark.integration
@pytest.mark.db_integration_test
def test_create_and_validate_user_fields(repository: FixtureDef) -> None:
    user_schema = CreateUserSchema(
        username="Henrique",
        email="Henrique@gmail.com",
        password="MinhaSenha123@2",
        confirm_password="MinhaSenha123@2",
    )

    repository.create_user(user_schema)  # type: ignore
    user = repository.select_user_by_email("Henrique@gmail.com")  # type: ignore
    expected = {"username": user.username, "email": user.email}

    assert expected == {"username": "Henrique", "email": "Henrique@gmail.com"}
