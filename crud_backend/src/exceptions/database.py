class DatabaseError(Exception):
    """Class inherited by all custom database exceptions"""

    def __init__(
        self, detail: str, status_code: int, original_exception: Exception | None = None
    ) -> None:
        super().__init__(detail)
        self.detail = detail
        self.status_code = status_code
        self.original_exception = original_exception


class ErrorRecordNotFound(DatabaseError):
    """Exception used to capture errors generated when records in database are not found."""

    pass


class ErrorEmailAlreadyExists(DatabaseError):
    """Exception used to capture errors generated when emails already existing in the database are requested for use by other users."""

    pass


class ErrorPerformingDatabaseOperation(DatabaseError):
    """Exception used to capture errors generated when operating records in the database."""

    pass
