import asyncio

from aiogram import Dispatcher, Bot

from project_configuration.configuration import Configuration

from handlers import get_user_router


async def main() -> None:
    config = Configuration()
    config.turn_on_logging()

    bot = Bot(token=config.get_telegram_bot_token())
    await bot.delete_webhook(drop_pending_updates=True)

    dp = Dispatcher(bot=bot)

    dp.include_routers(
        get_user_router()
    )

    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main())
