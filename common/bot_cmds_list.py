from aiogram.types import BotCommand

# команды для личных сообщений боту
private = [
    BotCommand(command='profile', description='Посмотреть свой профиль'),  # добавляем команду профиля
    BotCommand(command='achievements', description='Посмотреть свои достижения'),  # добавляем команду достижений
    BotCommand(command='goals', description='Просмотреть свои цели и желания'),  # добавляем команду целей
    # добавляем команду рутин
    BotCommand(command='routine', description='Посмотреть рутины (ежедневные/еженедельные задачи)'),
    BotCommand(command='top', description='Просмотреть топ пользователей'),  # добавляем команду топа
    BotCommand(command='subscribe', description='Оформить подписку для премиум-функций')  # добавляем команду подписки
]
