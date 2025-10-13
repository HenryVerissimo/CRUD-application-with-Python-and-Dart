from argon2 import PasswordHasher
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class User(Base):
    """User model to map the table of users in the database to a class in this project."""

    __tablename__ = "users"

    id: Mapped[int] = mapped_column("id", Integer(), primary_key=True, nullable=False)
    username: Mapped[str] = mapped_column("username", String(100), nullable=False)
    email: Mapped[str] = mapped_column("email", String(100), nullable=False, unique=True)
    password_hash: Mapped[str] = mapped_column("password_hash", String(250))

    def __init__(self, username: str, email: str, password: str) -> None:
        """Construct method this class.

        Args:
            username(str): User name.
            email(str): User email.
            password(str): User password.

        Attributes:
            username(str): User name.
            email(str): User email.
            password_hash(str): A hash of the user's password.
            ph(PasswordHasher): Instance used to create and verify password hashes.
        """

        self.username = username
        self.email = email
        self.password_hash = self._hashing_password(password)
        self.ph = PasswordHasher()

    def _hashing_password(self, password: str) -> str:
        """Create a hash of the user's password.

        Args:
            password(str): user password.

        Returns:
            str: Password hash.
        """

        hash = self.ph.hash(password, salt=bytes(self.id))

        return hash
    
    def verify_password(self,password: str) -> bool:
        """validates a password using the hash of the user's password.

        Args:
            password(str): The password to verify.

        Returns:
            bool: True if password is valid or False if not.
        """

        return  self.ph.verify(self.password_hash, password)
