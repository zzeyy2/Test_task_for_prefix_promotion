from questionary import Style


CHOICES = [
    'Добавить книгу',
    'Просмотреть все книги',
    'Просмотреть книги определенного жанра',
    'Поиск книги'
]

DISPLAYED_BOOKS_CHOICES = [
    'Удалить',
    'Назад'
]

QUESTIONARY_SETTINGS = {
    'qmark': '',
    'style': Style([
        ('qmark', 'fg:#673ab7 bold'),       # token in front of the question
        ('question', 'bold'),               # question text
        ('answer', 'fg:#f44336 bold'),      # submitted answer text behind the question
        ('pointer', 'fg:#673ab7 bold'),     # pointer used in select and checkbox prompts
        ('highlighted', 'fg:#673ab7 bold'), # pointed-at choice in select and checkbox prompts
        ('selected', 'fg:#cc5454'),         # style for a selected item of a checkbox
        ('separator', 'fg:#cc5454'),        # separator in lists
        ('instruction', ''),                # user instructions for select, rawselect, checkbox
        ('text', ''),                       # plain text
        ('disabled', 'fg:#858585 italic')   # disabled choices for select and checkbox prompts
    ])
}

IF_DATA_IS_UKNOWN = 'Не установлено'