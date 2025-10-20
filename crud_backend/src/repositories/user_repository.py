from typing import List

from src.models.user_model import User
from src.schemas.user_schemas import CreateUserSchema, UserUpdate
from src.database.connection_db_interface import ConnectionDBInterface


class UserRepository:
    """Responsible for performing queries and database operations related to Users."""

    def __init__(self, connection_db: ConnectionDBInterface) -> None:
        """construct method this class

        Args:
            connection_db(ConnectionDBInterface): any class database connection that implements this interface.

        Attributes:
            connection_db(ConnectionDBInterface): Context manager used to connect to the database in the methods.
        """

        self.connection_db = connection_db

    def create_user(self, user_schema: CreateUserSchema) -> User:
        """Creates a new user in the database.

        Args:
            user_schema(CreateUserSchema): Object with user data.

        Returns:
            User: New user created.
        """

        with self.connection_db as connection:
            new_user = User(
                username=user_schema.username,
                email=user_schema.email,
                password=user_schema.password,
            )

            connection.session.add(new_user)  # type: ignore
            connection.session.commit()  # type: ignore
            connection.session.refresh(new_user)  # type: ignore

            return new_user

    def select_user_by_email(self, user_email: str) -> User | None:
        """Select a user in databse by email.

        Args:
            user_email(str): User's unique email.

        Returns:
            User: Object with user data.
            None: if the user does not exist.
        """

        with self.connection_db as connection:
            user = (
                connection.session.query(User).filter(User.email == user_email).first()  # type: ignore
            )
            return user

    def select_user_by_id(self, user_id: int) -> User | None:
        with self.connection_db as connection:
            user = connection.session.query(User).filter(User.id == user_id).first()  # type: ignore

            return user

    def select_users(self) -> List[User]:
        """Select all users in the database.

        Returns:
            List[User]: a list of objects with all users in the database.
        """
        with self.connection_db as connection:
            users = connection.session.query(User).all()  # type: ignore

            return users

    def update_user(self, user_id: int, user_update_schema: UserUpdate) -> User | None:
        """Update user data in the database by unique id.

        Args:
            user_id(int): unique id of the user who will have their data updated.
            user_update_schema(UserUpdate): Object with user data that will be updated.

        Returns:
            User: User object with its data.
            None: if the user does not exist.
        """

        with self.connection_db as connection:
            user = connection.session.query(User).filter(User.id == user_id).first()  # type: ignore

            if user is not None:
                if user_update_schema.username is not None:
                    user.username = user_update_schema.username

                if user_update_schema.email is not None:
                    user.email = user_update_schema.email

                connection.session.commit()  # type: ignore
                connection.session.refresh(user)  # type: ignore

            return user

    def delete_user(self, user_id: int) -> None:
        """Delete user data in the database by unique id.

        Args:
            user_id(int): unique id of the user who will have their data deleted.
        """

        with self.connection_db as connection:
            user = connection.session.query(User).filter(User.id == user_id).first()  # type: ignore
            connection.session.delete(user)  # type: ignore
            connection.session.commit()  # type: ignore
