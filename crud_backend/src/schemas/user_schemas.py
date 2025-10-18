from pydantic import BaseModel, ConfigDict


class CreateUserSchema(BaseModel):
    """Data schema to create new users"""

    username: str
    email: str
    password: str
    confirm_password: str


class UserResponse(BaseModel):
    """Data schema to return the user in the response"""

    id: int
    username: str
    email: str

    model_config = ConfigDict(from_attributes=True)
