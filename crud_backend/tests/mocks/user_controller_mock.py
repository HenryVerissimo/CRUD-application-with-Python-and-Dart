from abc import ABC
from typing import List

from src.schemas.user_schemas import CreateUserSchema, UserResponse, UserUpdate


class UserControllerMock(ABC):
    pass


class MockingSuccessfulResponses(UserControllerMock):
    """mock of the UserController class used in the tests"""

    def create_user(self, user_schema: CreateUserSchema) -> UserResponse:
        user = UserResponse(
            id=1,
            username=user_schema.username,
            email=user_schema.email,
        )

        return user

    def get_all_users(self) -> List[UserResponse]:
        users = [
            UserResponse(id=1, username="UserTest1@", email="usertest1@gmail.com"),
            UserResponse(id=2, username="UserTest2@", email="usertest2@gmail.com"),
            UserResponse(id=3, username="UserTest3@", email="usertest3@gmail.com"),
        ]

        return users

    def update_user_data(
        self, user_id: int, user_update_schema: UserUpdate
    ) -> UserResponse | None:
        if (user_update_schema.username is not None) and (
            user_update_schema.email is not None
        ):
            user = UserResponse(
                id=int(user_id),
                username=user_update_schema.username,
                email=user_update_schema.email,
            )

            return user

    def delete_user_record(self, user_id: int) -> None:
        pass
