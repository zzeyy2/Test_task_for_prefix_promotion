from database import config
from database import models
from database import exec_files
from database.lib import books_db

import asyncio


async def init_models():
    async with exec_files.engine.begin() as conn:
        await conn.run_sync(models.Book.metadata.create_all)


asyncio.run(init_models())

__all__ = ["User", "engine", "config", "books_db"]
