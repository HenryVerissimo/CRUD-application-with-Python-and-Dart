from src.models.base import Base
from src.utils.create_model_tables import create_model_tables
from src.database.mysql.connection_mysql_db import CONNECTION_MYSQL


if __name__ == "__main__":
    create_model_tables(Base, CONNECTION_MYSQL)
