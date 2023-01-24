from aiogram import Dispatcher
from aiogram.types import Message

from lexicon.lexicon_ua import LEXICON_UA


async def send_answer(message: Message):
    await message.answer(text=LEXICON_UA['other_answer'])


def register_other_handlers(dp: Dispatcher):
    dp.register_message_handler(send_answer)
