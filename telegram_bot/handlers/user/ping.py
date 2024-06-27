from aiogram import html, types


async def ping(msg: types.Message) -> None:
    if msg.from_user is None:
        return
    m = [
        '🏀',
        '<b>pong</b>'
    ]
    await msg.answer("\n".join(m))
