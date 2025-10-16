from src.models.user_model import User
from src.schemas.user_schemas import CreateUserSchema
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

    def select_user_by_email(self, user_email: str) -> User:
        """Select a user in databse by email.

        Args:
            user_email(str): User's unique email.

        Returns:
            User: Object with user data.
        """

        with self.connection_db as connection:
            user = (
                connection.session.query(User).filter(User.email == user_email).first()
            )  # type: ignore
            return user
