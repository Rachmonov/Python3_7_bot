from typing import Union
from aiogram import Bot

async def tekshirish(user_id,kanal_link):
    user = Bot.get_current()
    checking = await  user.get_chat_member(chat_id=kanal_link,user_id=user_id)
    return checking.is_chat_member()