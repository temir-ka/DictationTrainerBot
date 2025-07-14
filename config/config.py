from dataclasses import dataclass 
from environs import Env


@dataclass
class TgBot:
    token: str  # A token for accessing the telegram bot


@dataclass
class Config:
    bot: TgBot


def load_config(path: str | None=None) -> Config:
    env: Env = Env()
    env.read_env(path)

    return Config(
        bot=TgBot(token=env("BOT_TOKEN"))
    )
