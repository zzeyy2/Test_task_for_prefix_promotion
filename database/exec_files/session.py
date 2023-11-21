from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.orm.session import Session
from database.exec_files import engine

AsyncSession: Session = async_sessionmaker(bind=engine)
