from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from lexicon.lexicon import LEXICON_RU


user_router = Router()


@user_router.message(CommandStart())
async def process_start_command(message: Message):
    user_name = message.from_user.first_name
    text = LEXICON_RU["/start"].format(name=user_name)
    await message.answer(text)