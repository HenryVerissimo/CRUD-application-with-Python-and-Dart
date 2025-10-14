from fastapi.responses import JSONResponse

from src.schemas.user_schemas import CreateUserSchema
from src.repositories.user_repository import UserRepository
from src.database.mysql.connection_mysql_db import CONNECTION_MYSQL


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
