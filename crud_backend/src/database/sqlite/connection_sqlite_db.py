from typing import Self
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker

from src.database.connection_db_interface import ConnectionDBInterface


class ConnectionSqliteDB(ConnectionDBInterface):
    """Responsible for connecting to the SQLite database."""

    def __init__(self, database: str, path: str | None = None) -> None:
        """Construct methos this class.

        Args:
            database(str): Database name.
            path(str | None): Optional path to save the database file.

        Attributes:
            session(Session | None): Database connection session.
            engine(Engine | None): Mechanism to connect to a database.
        """

        self.session: Session | None = None
        self.engine: Engine | None = None
        self._database: str | None = database
        self._path: str | None = None

    def _create_engine(self) -> None:
        """Creates a engine to connect to the database using the URL."""

        if self._path:
            self.engine = create_engine(f"sqlite:////{self._path}/{self._database}.db")

        self.engine = create_engine(f"sqlite:///{self._database}.db")

    def create_connection(self):
        """create a connection session with the database.

        Returns:
            Session: session with the database.
        """
        if not self.engine:
            self._create_engine()

        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def __enter__(self) -> Self:
        """calls the session creation method.

        Returns:
            Self: the instance self.
        """

        self.create_connection()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Close session with database and delete the engine"""

        if self.session:
            self.session.close()

        if self.engine:
            self.engine = None
