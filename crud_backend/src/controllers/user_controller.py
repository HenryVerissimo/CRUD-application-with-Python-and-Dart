from typing import List
from fastapi import status

from src.models.user_model import User
from src.repositories.user_repository import UserRepository
from src.database.mysql.connection_mysql_db import CONNECTION_MYSQL
from src.schemas.user_schemas import CreateUserSchema, UserUpdate
from src.exceptions.database import (
    ErrorEmailAlreadyExists,
    ErrorRecordNotFound,
    ErrorPerformingDatabaseOperation,
)


class UserController:
    """Responsible for grouping domain rules related to users."""

    def __init__(self) -> None:
        """Construct method this class.

        Attributes:
            user_repo(UserRepository): User repository instantiation for domain rules.
        """
        self.user_repo = UserRepository(CONNECTION_MYSQL)

    def create_user(self, user_schema: CreateUserSchema) -> User:
        """Create a new user in database.

        Args: user_schema(CreateUserSchema): Object with user data.

        Returns:
            User: User object with its data.
        """

        try:
            user = self.user_repo.select_user_by_email(user_email=user_schema.email)

            if user:
                raise ErrorEmailAlreadyExists(
                    detail="This email has already been used",
                    status_code=status.HTTP_409_CONFLICT,
                )

            data = self.user_repo.create_user(user_schema)

        except Exception as error:
            raise ErrorPerformingDatabaseOperation(
                detail="Error trying to create user in the database",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                original_exception=error,
            )

        return data

    def get_all_users(self) -> List[User]:
        """Get all users in database.

        Retuns:
            List[User]: a list of objects with all users in the database.
        """
        try:
            data = self.user_repo.select_users()

        except Exception as error:
            raise ErrorPerformingDatabaseOperation(
                detail="Error trying to select users from database",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                original_exception=error,
            )

        return data

    def update_user_data(self, user_id: int, user_update_schema: UserUpdate) -> User:
        """update user data in the database.

        Args:
            user_id(int): unique id of the user who will have their data updated.
            user_update_schema(UserUpdate): Object with user data that will be updated.

        Returns:
            User: User object with its data.
        """

        try:
            if user_update_schema.email is not None:
                user = self.user_repo.select_user_by_email(user_update_schema.email)

                if user is not None:
                    raise ErrorEmailAlreadyExists(
                        detail="This email has already been used",
                        status_code=status.HTTP_409_CONFLICT,
                    )

            data = self.user_repo.update_user(user_id, user_update_schema)

            if not data:
                raise ErrorRecordNotFound(
                    detail="Record not found in database",
                    status_code=status.HTTP_404_NOT_FOUND,
                )

            return data

        except Exception as error:
            raise ErrorPerformingDatabaseOperation(
                detail="Error trying to update user from database",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                original_exception=error,
            )
