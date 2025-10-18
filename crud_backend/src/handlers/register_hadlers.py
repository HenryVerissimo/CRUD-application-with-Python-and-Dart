from fastapi import FastAPI

from src.exceptions.database import DatabaseError
from .database_handler import database_error_handler


def register_exception_handeler(app: FastAPI) -> None:
    """Configure all custom exception handlers in the application.

    Args:
        app(FastAPI): Main intance the apllication.
    """

    app.add_exception_handler(DatabaseError, database_error_handler)  # type: ignore
