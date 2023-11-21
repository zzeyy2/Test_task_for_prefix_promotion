from database import books_db
from config import CHOICES, QUESTIONARY_SETTINGS
from utils import display_books, ask_book_details

import asyncio
import questionary


async def main():
    while True:
        select = questionary.select(
            f"Выберите действие: ", choices=CHOICES, **QUESTIONARY_SETTINGS
        )
        choice = await select.ask_async()

        if choice == CHOICES[0]:
            name, author, description, genre = await ask_book_details()
            if name:
                await books_db.add_book(name, author, description, genre)

        elif choice == CHOICES[1]:
            all_books = await books_db.get_all_books()
            await display_books(all_books)

        elif choice == CHOICES[2]:
            genre = await questionary.text(
                "Введите жанр: ", **QUESTIONARY_SETTINGS
            ).ask_async()
            genre_filtred_books = await books_db.get_all_genre_books(genre)
            await display_books(genre_filtred_books)

        elif choice == CHOICES[3]:
            query = await questionary.text(
                "Введите запрос: ", **QUESTIONARY_SETTINGS
            ).ask_async()
            searched_books = await books_db.search_books(query)
            await display_books(searched_books)


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
