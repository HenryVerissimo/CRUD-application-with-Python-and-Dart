from sqlalchemy.orm import DeclarativeBase

from src.database.connection_db_interface import ConnectionDBInterface


def create_model_tables(
    base: DeclarativeBase, database_class: ConnectionDBInterface
) -> None:
    """This function creates all the Model tables in the database configured in SQLALchemy.

    Args:
        base(DeclarativeBase): Base Instance used for create model classes.
        database_class(ConnectionDBInterface): any class database connection that implements this interface.
    """

    database_class.create_connection()
    engine = database_class.engine  # type: ignore
    base.metadata.create_all(bind=engine)  # type: ignore
