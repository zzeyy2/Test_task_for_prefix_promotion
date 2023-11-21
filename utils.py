import re, questionary, os
from typing import List, NoReturn

from config import QUESTIONARY_SETTINGS, IF_DATA_IS_UKNOWN, DISPLAYED_BOOKS_CHOICES
from database import books_db


def find_book_name(string: str):
    pattern = r": (.+?) \|"
    return re.findall(pattern, string)[0]


def find_book_author(string: str):
    pattern = r": (.*?)$"
    return re.findall(pattern, string, re.MULTILINE)[0]


async def ask_book_details() -> tuple:
    os.system("cls||clear")
    name = await questionary.text(
        "Введите имя книги: ", **QUESTIONARY_SETTINGS
    ).ask_async()
    if not name:
        questionary.print("Имя книги обязательно!")
        return None, None, None, None

    author = await questionary.text(
        "Введите автора книги: ", **QUESTIONARY_SETTINGS
    ).ask_async()
    description = await questionary.text(
        "Введите описание книги: ", **QUESTIONARY_SETTINGS
    ).ask_async()
    genre = await questionary.text(
        "Введите жанр книги: ", **QUESTIONARY_SETTINGS
    ).ask_async()
    os.system("cls||clear")
    return name, author, description, genre


async def display_books(all_books: List[tuple]) -> NoReturn:
    """Отобразить список книг

    Args:
        all_books (List[tuple]): Список книг
    """
    os.system("cls||clear")

    formatted_books = [
        f"Имя: {book_data[0]} | Автор: {book_data[1] if book_data[1] else IF_DATA_IS_UKNOWN}"
        for book_data in all_books
    ]
    formatted_books.append("Назад")
    select = questionary.select(
        "Книги: " if all_books else "Книг нет",
        choices=formatted_books,
        instruction=None,
        **QUESTIONARY_SETTINGS,
    )
    choice = await select.ask_async()
    if choice == "Назад":
        os.system("cls||clear")
        return
    os.system("cls||clear")
    book_name = find_book_name(choice)
    book_author = find_book_author(choice)
    book_description = await books_db.get_book_desctiption(book_name)
    book_genre = await books_db.get_book_genre(book_name)

    choice = await questionary.select(
        (
            f"Название книги: {book_name}\n"
            f"Автор книги: {book_author}\n"
            f"Описание: {book_description if book_description else IF_DATA_IS_UKNOWN}\n"
            f"Жанр: {book_genre if book_genre else IF_DATA_IS_UKNOWN}"
        ),
        choices=DISPLAYED_BOOKS_CHOICES,
    ).ask_async()
    if choice == DISPLAYED_BOOKS_CHOICES[0]:
        await books_db.delete_book(book_name)
    if choice == DISPLAYED_BOOKS_CHOICES[1]:
        os.system("cls||clear")
        return
