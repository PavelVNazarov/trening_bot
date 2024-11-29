# subscription.py
from aiogram import Bot

async def check_subscription(user_id, bot: Bot):
    try:
        member = await bot.get_chat_member(chat_id='@your_channel_id', user_id=user_id)
        return member.status in ['member', 'administrator', 'creator']
    except Exception:
        return False