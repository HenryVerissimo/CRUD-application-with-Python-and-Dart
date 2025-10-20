from typing import List
from fastapi import status
from fastapi import APIRouter, HTTPException

from src.models.user_model import User
from src.controllers.user_controller import UserController
from src.schemas.user_schemas import CreateUserSchema, UserResponse, UserUpdate

from src.utils import regex_validations as regex


user_router = APIRouter(prefix="/users", tags=["users"])


@user_router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user_schema: CreateUserSchema) -> User:
    """Creates a new user in the databse."""

    if not regex.validate_email(user_schema.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The email pattern is not valid",
        )

    if not regex.validate_password(user_schema.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The password pattern is not valid",
        )

    if not regex.validate_username(user_schema.username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The username pasttern is not valid",
        )

    controller = UserController()
    response = controller.create_user(user_schema)

    return response


@user_router.get("/", response_model=List[UserResponse], status_code=status.HTTP_200_OK)
async def get_users() -> List[User]:
    """Select all users in the database."""

    controller = UserController()
    response = controller.get_all_users()

    return response


@user_router.patch("/update/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user_update_schema: UserUpdate) -> User:
    """Update user data in the database."""

    if user_update_schema.email is not None:
        if not regex.validate_email(user_update_schema.email):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="The email pattern is not valid",
            )

    if user_update_schema.username is not None:
        if not regex.validate_username(user_update_schema.username):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="The username pasttern is not valid",
            )

    controller = UserController()
    response = controller.update_user_data(user_id, user_update_schema)

    return response


@user_router.delete("/delete/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int) -> None:
    """Delete user in the database"""

    controller = UserController()
    controller.delete_user_record(user_id)
