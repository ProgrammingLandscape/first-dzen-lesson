from aiogram import Router


def get_user_router() -> Router:
    user_router = Router()

    from .command_handlers import on_start

    user_router.include_routers(
        on_start.router
    )

    return user_router
