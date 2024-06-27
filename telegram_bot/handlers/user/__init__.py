from aiogram import Router
from aiogram.filters import CommandStart, Command

from . import start, ping
from filters import ChatTypeFilter


def prepare_router() -> Router:
    user_router = Router()
    user_router.message.filter(ChatTypeFilter("private"))

    user_router.message.register(start.start, CommandStart())
    user_router.message.register(ping.ping, Command('ping'))

    return user_router
