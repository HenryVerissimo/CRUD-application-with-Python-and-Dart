import os
import pytest

from typing import Generator, cast

from src.models.base import Base
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
