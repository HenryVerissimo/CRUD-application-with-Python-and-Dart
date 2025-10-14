from fastapi import FastAPI


def create_app() -> FastAPI:
    """FastAPI application Factory.

    Returns:
        FastAPI: An instance of the FastAPI application.
    """

    app = FastAPI()

    from src.routes.user_routes import user_router

    app.include_router(user_router)

    return app


app = create_app()
