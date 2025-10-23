from src.controllers.user_controller import UserController


def get_user_controller() -> UserController:
    controller = UserController()
    return controller
