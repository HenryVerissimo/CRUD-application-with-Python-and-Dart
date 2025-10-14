import os
import sys

from typing import cast
from typing import Self
from decouple import config
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import Session, sessionmaker


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../configs")))

from src.database.connection_db_interface import ConnectionDBInterface


class ConnectionMysqlDB(ConnectionDBInterface):
    """Responsible for connecting to the MySQL database."""

    def __init__(
        self,
        driver_name: str,
        username: str,
        password: str,
        host: str,
        port: str,
        database: str,
    ) -> None:
        """Construct method this class.

        Args:
            driver_name(str): Name of the driver use to connect to MySQl database.
            username(str): Username what you use to connect to MySQL database.
            password(str): Password what you use to connect to MySQl database.
            host(str): Host where your MySQL database is hosted.
            port(str): Port that your MySQL database is listining to.
            database(str): Database name.

        Attributes:
            session(Session | None): Database connection session.
            engine(Engine | None): Mechanism to connect to a database.
            _string_connection(str): URL of connection to a database.

        """
        self.session: Session | None = None
        self.engine: Engine | None = None
        self._string_conection = (
            f"mysql+{driver_name}://{username}:{password}@{host}:{port}/{database}"
        )

    def _create_engine(self) -> None:
        """Creates a engine to connect to the database using the URL."""

        self.engine = create_engine(self._string_conection)

    def create_connection(self) -> None:
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


USERNAME_DB = config("USERNAME_DB")
PASSWORD_DB = config("PASSWORD_DB")
HOST_DB = config("HOST_DB")
PORT_DB = config("PORT_DB")
DATABASE = config("DATABASE")


CONNECTION_MYSQL = ConnectionMysqlDB(
    driver_name="pymysql",
    username=cast(str, USERNAME_DB),
    password=cast(str, PASSWORD_DB),
    host=cast(str, HOST_DB),
    port=cast(str, PORT_DB),
    database=cast(str, DATABASE),
)  # type: ignore
