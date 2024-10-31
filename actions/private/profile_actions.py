async def get_profile_text(user_id: int):
    # Пример данных профиля. В дальнейшем заменим на реальные данные из базы данных.
    profile_data = {
        "username": "@trump",
        "level": "Школотрон",
        "completed_goals": 2,
        "total_goals": 5,
        "currency_balance": 1000,
        "diamonds": 14,
        "health": "3 / 3",
        "recent_activity": [
            {"description": "Вы зарегистрировались!", "time_ago": "16 мин назад", "xp": "+30xp"},
            {"description": "Вы выполнили цель", "time_ago": "2 мин назад", "xp": "+300xp"},
            {"description": "Новое достижение", "time_ago": "вчера", "xp": "+30xp"}
        ]
    }

    # Формируем текст профиля
    profile_text = f"""
    <b>{profile_data['username']}</b>
    Уровень: {profile_data['level']}
    Выполнено: {profile_data['completed_goals']} / {profile_data['total_goals']} целей
    Здоровье: {profile_data['health']}
    Баланс: {profile_data['currency_balance']} 💰 | 💎 {profile_data['diamonds']}

    <b>Последние действия:</b>
    """
    for activity in profile_data["recent_activity"]:
        profile_text += f"{activity['description']} - {activity['time_ago']} ({activity['xp']})\n"

    return profile_text


async def get_achievements_text(user_id: int):
    # Пример данных достижений. В будущем заменим на реальные данные из базы.
    achievements_data = {
        "completed": [
            {"title": "Первое достижение", "description": "Получено за первый выполненный вызов", "xp": 100},
            {"title": "Целеустремлённый", "description": "Выполнено 5 целей", "xp": 300}
        ],
        "incomplete": [
            {"title": "Покоритель", "description": "Завершите 10 вызовов", "xp": 500},
            {"title": "Мастер", "description": "Завершите 20 вызовов", "xp": 1000}
        ]
    }

    # Формируем текст достижений
    achievements_text = "<b>Полученные достижения:</b>\n"
    for ach in achievements_data["completed"]:
        achievements_text += f"🏆 {ach['title']}: {ach['description']} (+{ach['xp']}xp)\n"

    achievements_text += "\n<b>Достижения в процессе:</b>\n"
    for ach in achievements_data["incomplete"]:
        achievements_text += f"🔒 {ach['title']}: {ach['description']} (+{ach['xp']}xp)\n"

    return achievements_text


async def get_goals_text(user_id: int):
    # Пример данных целей и желаний. В будущем заменим на реальные данные из базы.
    goals_data = {
        "active": [
            {"title": "Изучить Python", "description": "Пройти курс по Python", "progress": "50%"},
            {"title": "Читать книги", "description": "Прочитать 10 книг", "progress": "30%"}
        ],
        "completed": [
            {"title": "Сделать утреннюю зарядку", "description": "Выполнено за 30 дней", "progress": "100%"}
        ]
    }

    # Формируем текст для целей
    goals_text = "<b>Текущие цели:</b>\n"
    for goal in goals_data["active"]:
        goals_text += f"🎯 {goal['title']}: {goal['description']} (Прогресс: {goal['progress']})\n"

    goals_text += "\n<b>Завершенные цели:</b>\n"
    for goal in goals_data["completed"]:
        goals_text += f"✅ {goal['title']}: {goal['description']} (Прогресс: {goal['progress']})\n"

    return goals_text


async def get_routine_text(user_id: int):
    # Пример данных для рутин. В будущем заменим на реальные данные из базы.
    routine_data = {
        "daily": [
            {"title": "Утренняя зарядка", "description": "Сделать зарядку утром", "completed": False},
            {"title": "Пить воду", "description": "Выпить 8 стаканов воды", "completed": True}
        ],
        "weekly": [
            {"title": "Чтение", "description": "Прочитать одну главу книги", "completed": False},
            {"title": "Уборка", "description": "Провести уборку в квартире", "completed": True}
        ]
    }

    # Формируем текст для рутины
    routine_text = "<b>Ежедневные задачи:</b>\n"
    for task in routine_data["daily"]:
        status = "✅ Выполнено" if task["completed"] else "🔲 Не выполнено"
        routine_text += f"{task['title']}: {task['description']} ({status})\n"

    routine_text += "\n<b>Еженедельные задачи:</b>\n"
    for task in routine_data["weekly"]:
        status = "✅ Выполнено" if task["completed"] else "🔲 Не выполнено"
        routine_text += f"{task['title']}: {task['description']} ({status})\n"

    return routine_text


async def get_top_users():
    # Пример данных для топа пользователей. В будущем заменим на реальные данные из базы.
    top_users = [
        {"username": "@player1", "score": 1500, "rank": 1},
        {"username": "@player2", "score": 1200, "rank": 2},
        {"username": "@player3", "score": 1000, "rank": 3},
        {"username": "@player4", "score": 800, "rank": 4},
        {"username": "@player5", "score": 600, "rank": 5},
    ]

    # Формируем текст для топа пользователей
    top_text = "<b>Топ пользователей:</b>\n"
    for user in top_users:
        top_text += f"{user['rank']}. {user['username']} - {user['score']} очков\n"

    return top_text
