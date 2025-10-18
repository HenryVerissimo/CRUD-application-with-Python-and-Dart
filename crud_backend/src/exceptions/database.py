class DatabaseError(Exception):
    """Class inherited by all custom database exceptions"""

    def __init__(
        self, detail: str, status_code: int, original_exception: Exception
    ) -> None:
        super().__init__(detail)
        self.detail = detail
        self.status_code = status_code
        self.original_exception = original_exception


class ErrorSelectingRecordsFromDatabase(DatabaseError):
    """Exception used to capture errors generated when selecting records in the database."""

    pass
