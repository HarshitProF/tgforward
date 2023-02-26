from . import user
from .routes import routes
from telethon import utils
import asyncio
num='7084522428'
async def user_auth():
    await user.connect()
    if not await user.is_user_authorized():
        user.start(phone=utils.parse_phone(num))
    async with user:
        user.add_event_handler(routes.send)
        await user.run_until_disconnected()
asyncio.run(user_auth())
