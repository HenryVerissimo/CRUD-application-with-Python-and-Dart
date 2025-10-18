from typing import List
from fastapi import status
from fastapi import APIRouter, HTTPException

from src.schemas.user_schemas import CreateUserSchema, UserResponse
from src.controllers.user_controller import UserController

from src.utils import regex_validations as regex


user_router = APIRouter(prefix="/users", tags=["users"])


@user_router.post("/")
async def create_user(user_schema: CreateUserSchema):
    """Creates a new user in the databse."""

    if not regex.validate_email(user_schema.email):
        raise HTTPException(status_code=400, detail="The email pattern is not valid")

    if not regex.validate_password(user_schema.password):
        raise HTTPException(status_code=400, detail="The password pattern is not valid")

    if not regex.validate_username(user_schema.username):
        raise HTTPException(
            status_code=400, detail="The username pasttern is not valid"
        )

    controller = UserController()
    response = controller.create_user(user_schema)

    return response


@user_router.get("/", response_model=List[UserResponse], status_code=status.HTTP_200_OK)
async def get_users():
    controller = UserController()
    response = controller.get_all_users()

    return response
