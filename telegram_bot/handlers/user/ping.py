from aiogram import types

from connections.api.ping import PingPong


async def ping(msg: types.Message) -> None:
    if msg.from_user is None:
        return

    pp = PingPong()

    if await pp.get_ping() == 'pong':
        m = [
            '🏀',
            '<b>pong</b>'
        ]
        await msg.answer("\n".join(m))
