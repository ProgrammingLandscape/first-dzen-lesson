import logging
import os

from dotenv import load_dotenv


class Configuration:
    def __init__(self):
        load_dotenv()

    @staticmethod
    def turn_on_logging():
        logging.basicConfig(
            level=logging.INFO,
            format="{%(name)s} %(asctime)s [%(levelname)s]    ->    %(message)s"
        )

    @staticmethod
    def get_telegram_bot_token():
        return os.getenv("TELEGRAM_BOT_TOKEN")
