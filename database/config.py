import os

DATABASE_DIR_NAME = os.path.dirname(os.path.abspath(__file__))
DATABASE_URL = f'sqlite+aiosqlite:///{os.path.join(DATABASE_DIR_NAME, "database.db")}'
