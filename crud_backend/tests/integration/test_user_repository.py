import os
import pytest

from pytest import FixtureDef
from typing import Generator, cast

from src.models.base import Base
from src.schemas.user_schemas import CreateUserSchema
from src.repositories.user_repository import UserRepository
from src.utils.create_model_tables import create_model_tables
from src.database.connection_db_interface import ConnectionDBInterface
from src.database.sqlite.connection_sqlite_db import ConnectionSqliteDB


@pytest.fixture
def connection_db() -> Generator[ConnectionDBInterface, None, None]:
    database_test = ConnectionSqliteDB("test")
    create_model_tables(Base, database_test)

    try:
        yield database_test

    finally:
        os.remove(os.path.abspath("test.db"))


@pytest.fixture
def repository(connection_db) -> UserRepository:
    return UserRepository(cast(ConnectionDBInterface, connection_db))


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
