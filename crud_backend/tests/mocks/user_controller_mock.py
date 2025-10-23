from abc import ABC
from src.schemas.user_schemas import CreateUserSchema, UserResponse


class UserControllerMock(ABC):
    pass


class CreateUserSuccessfully(UserControllerMock):
    """mock of the UserController class used in the tests"""

    def create_user(self, user_schema: CreateUserSchema) -> UserResponse:
        user = UserResponse(
            id=1,
            username=user_schema.username,
            email=user_schema.email,
        )

        return user
