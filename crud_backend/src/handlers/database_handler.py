from fastapi import Request
from fastapi.responses import JSONResponse

from src.exceptions.database import DatabaseError


async def database_error_handler(request: Request, exc: DatabaseError) -> JSONResponse:
    """Capture and tret database errors in application.

    Args:
        request(Request): Request object containing information about the HTTP request that caused the error.
        exc(DatabaseError): Exception object that caught the error.
    """

    payload = {"message": exc.detail}
    return JSONResponse(content=payload, status_code=exc.status_code)
