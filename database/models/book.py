from sqlalchemy import Column
from sqlalchemy.sql import sqltypes as types
from database.models import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(types.Integer, primary_key=True)
    name = Column(types.String, nullable=False, unique=True)
    author = Column(types.String)
    description = Column(types.String)
    genre = Column(types.String)
