from typing import List
from fastapi import status
from fastapi.responses import JSONResponse

from src.models.user_model import User
from src.repositories.user_repository import UserRepository
from src.database.mysql.connection_mysql_db import CONNECTION_MYSQL
from src.exceptions.database import ErrorSelectingRecordsFromDatabase
from src.schemas.user_schemas import CreateUserSchema


class UserController:
    """Responsible for grouping domain rules related to users."""

    def __init__(self) -> None:
        """Construct method this class.

        Attributes:
            user_repo(UserRepository): User repository instantiation for domain rules.
        """
        self.user_repo = UserRepository(CONNECTION_MYSQL)

    def create_user(self, user_schema: CreateUserSchema) -> JSONResponse:
        """Create a new user in database.

        Args: user_schema(CreateUserSchema): Object with user data.

        Returns:
            JsonResponse: Response with a successfully message, id and username.
        """
        data = self.user_repo.create_user(user_schema)

        payload = {
            "message": "User successfully created",
            "data": {"id": data.id, "username": data.username},
        }
        return JSONResponse(content=payload, status_code=200)

    def get_all_users(self) -> List[User]:
        """Get all users in database.

        Retuns:
            List[User]: a list of objects with all users in the database.
        """
        try:
            data = self.user_repo.select_users()

        except Exception as error:
            raise ErrorSelectingRecordsFromDatabase(
                detail="Error trying to select users from database",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                original_exception=error,
            )

        return data
