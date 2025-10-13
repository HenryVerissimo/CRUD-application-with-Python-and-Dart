from pydantic import BaseModel


class CreateUserSchema(BaseModel):
    """Data schema to create new users"""

    username: str
    email: str
    password: str
    confirm_password: str
