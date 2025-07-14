import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config.config import Config, load_config
from handlers.user_handlers import user_router
from handlers.other_handlers import other_router


# The function of configuring and launching the bot
async def main():
    config: Config = load_config()

    
    bot = Bot(
        token=config.bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()


    dp.include_router(user_router)
    dp.include_router(other_router)


    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())