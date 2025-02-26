import states
from aiogram import html, types
from aiogram.fsm.context import FSMContext


async def start(msg: types.Message, state: FSMContext) -> None:
    if msg.from_user is None:
        return
    m = [
        f'Hello, <a href="tg://user?id={msg.from_user.id}">{html.quote(msg.from_user.full_name)}</a>!',
        'Send /ping 🏓'
    ]
    await msg.answer("\n".join(m))
    await state.set_state(states.user.UserMainMenu.menu)
