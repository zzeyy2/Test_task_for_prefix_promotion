from database.models import Book
from database.exec_files import AsyncSession

from typing import NoReturn, List, Tuple
from sqlalchemy import select, or_


async def add_book(
    name: str, author: str = "", description: str = "", genre: str = ""
) -> NoReturn:
    """Добавить книгу в базу данных

    Args:
        name (str): Имя книги
        author (str): Автор книги
        description (str): Описание книги
        genre (str): Жанр книги"""

    async with AsyncSession() as session:
        session.add(
            Book(name=name, author=author, description=description, genre=genre)
        )
        await session.commit()


async def get_all_books() -> List[Tuple]:
    """Получить список книг (Название, Автор)"""
    async with AsyncSession() as session:
        stmt = await session.execute((select(Book.name, Book.author)))
        return stmt.all()


async def get_all_genre_books(genre: str) -> List[Tuple]:
    """Получить список книг (Название, Автор) По определенному жанру"""
    async with AsyncSession() as session:
        stmt = await session.execute(
            (select(Book.name, Book.author).where(Book.genre == genre))
        )
        return stmt.all()


async def get_book_desctiption(book_name: str) -> List[Tuple]:
    """Получение автора книги"""
    async with AsyncSession() as session:
        stmt = await session.execute(
            (select(Book.description).where(Book.name == book_name))
        )
        return stmt.scalar()


async def get_book_genre(book_name: str) -> List[Tuple]:
    """Получение жанр книги"""
    async with AsyncSession() as session:
        stmt = await session.execute((select(Book.genre).where(Book.name == book_name)))
        return stmt.scalar()


async def search_books(query: str) -> List[Tuple]:
    """Поиск книги по имени и автору. Возвращает Название, Автор"""
    async with AsyncSession() as session:
        stmt = await session.execute(
            select(Book.name, Book.author).where(
                or_(Book.name.like(f"%{query}%"), Book.author.like(f"%{query}%"))
            )
        )
        return stmt.all()


async def delete_book(book_name: str) -> NoReturn:
    """Поиск книги по имени и автору. Возвращает Название, Автор"""
    async with AsyncSession() as session:
        obj = await session.execute(select(Book).where(Book.name == book_name))
        obj = obj.scalar_one()
        print(obj)
        await session.delete(obj)
        await session.commit()
