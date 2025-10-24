from fastapi import FastAPI

from src.handlers.register_hadlers import register_exception_handeler


def create_app() -> FastAPI:
    """FastAPI application Factory.

    Returns:
        FastAPI: An instance of the FastAPI application.
    """

    app = FastAPI()

    from src.routes.user_routes import user_router

    register_exception_handeler(app)
    app.include_router(user_router)

    return app


app = create_app()
