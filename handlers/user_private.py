# обработчики событий, которые относятся к общению бота с пользователем в личке

import os
from aiogram import F, types, Router
# импортируем инлайн-клавиатуры
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
# для обработки HTML
from aiogram.enums import ParseMode
# импортируем систему фильтрации сообщений и для работы с командами
from aiogram.filters import CommandStart, Command, or_f, StateFilter
# импортируем библиотеки для работы со стояниями
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from datetime import datetime
# импортируем классы для форматирования текста
from aiogram.utils.formatting import as_list, as_marked_section, Bold
import aiohttp  # Асинхронная библиотека для HTTP-запросов

# наши импорты
# импортируем фильтр для определения личка, группа, супергруппа
from filters.chat_types import ChatTypeFilter
# импортируем ответные клавиатуры
from kbds.reply import get_keyboard
# импортируем глобальные переменные
from singleton import global_vars
# импортируем наши функции для лички
from actions.private import profile_actions

# создаем отдельный роутер для сообщений лички
user_private_router = Router()
# подключаем фильтр для определения, где будет работать роутер (в личке, в группе, супергруппе)
user_private_router.message.filter(ChatTypeFilter(['private']))

# Словарь для клавиатур (пример)
KEYBOARDS = {
    "user": get_keyboard("Проверить онлайн", placeholder="Выберите действие", sizes=(1,)),
    "social_media": get_keyboard("VK", placeholder="Выберите соцсеть", sizes=(1,)),
    "subscribe": get_keyboard("Подписаться", "Отписаться", "Отменить", placeholder="Выберите действие",
                              sizes=(1, 1, 1)),
    "back": get_keyboard("Назад", "Отменить", placeholder="Выберите действие", sizes=(1, 1)),
    "cancel": get_keyboard("Отменить", placeholder="Выберите действие", sizes=(1,))
}


# Вспомогательная функция для отправки ответов с клавиатурой
async def send_message_with_keyboard(message: types.Message, text: str, keyboard_type: str) -> None:
    await message.answer(text, reply_markup=KEYBOARDS[keyboard_type])


# Состояния для процесса броска вызова
class ChallengeStates(StatesGroup):
    choose_opponent = State()
    set_conditions = State()
    set_bet = State()
    set_deadline = State()


# Обработчик для команды /start
@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await send_message_with_keyboard(
        message,
        "Привет, я бот мотиватор!",
        # тип клавиатуры из словаря
        "user"
    )


# Обработчик для команды /profile
@user_private_router.message(Command("profile"))
async def profile_cmd(message: types.Message):
    # Вызов функции через модуль
    profile_text = await profile_actions.get_profile_text(message.from_user.id)

    # Кнопка для броска вызова
    challenge_button = InlineKeyboardButton(text="Бросить вызов", callback_data="challenge")
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[challenge_button]])

    await message.answer(profile_text, reply_markup=keyboard, parse_mode=ParseMode.HTML)


# Обработчик для команды /achievements
@user_private_router.message(Command("achievements"))
async def achievements_cmd(message: types.Message):
    achievements_text = await profile_actions.get_achievements_text(message.from_user.id)

    # Кнопка для добавления достижения
    add_achievement_button = InlineKeyboardButton(text="Добавить достижение", callback_data="add_achievement")
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[add_achievement_button]])

    await message.answer(achievements_text, reply_markup=keyboard, parse_mode=ParseMode.HTML)


# Обработчик для кнопки "Добавить достижение"
@user_private_router.callback_query(lambda c: c.data == "add_achievement")
async def add_achievement(callback_query: types.CallbackQuery):
    await callback_query.message.answer("Введите описание для нового достижения.")


# Обработчик для команды /goals
@user_private_router.message(Command("goals"))
async def goals_cmd(message: types.Message):
    goals_text = await profile_actions.get_goals_text(message.from_user.id)

    # Кнопка для добавления новой цели
    add_goal_button = InlineKeyboardButton(text="Добавить цель", callback_data="add_goal")
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[add_goal_button]])

    await message.answer(goals_text, reply_markup=keyboard, parse_mode=ParseMode.HTML)


# Обработчик для кнопки "Добавить цель"
@user_private_router.callback_query(lambda c: c.data == "add_goal")
async def add_goal(callback_query: types.CallbackQuery):
    await callback_query.message.answer("Введите описание для новой цели.")


# Обработчик для команды /routine
@user_private_router.message(Command("routine"))
async def routine_cmd(message: types.Message):
    routine_text = await profile_actions.get_routine_text(message.from_user.id)

    # Кнопка для подтверждения выполнения задачи
    confirm_task_button = InlineKeyboardButton(text="Подтвердить выполнение задачи", callback_data="confirm_task")
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[confirm_task_button]])

    await message.answer(routine_text, reply_markup=keyboard, parse_mode=ParseMode.HTML)


# Обработчик для кнопки "Подтвердить выполнение задачи"
@user_private_router.callback_query(lambda c: c.data == "confirm_task")
async def confirm_task(callback_query: types.CallbackQuery):
    await callback_query.message.answer("Введите название задачи, которую вы хотите подтвердить как выполненную.")


# Обработчик для команды /top
@user_private_router.message(Command("top"))
async def top_cmd(message: types.Message):
    top_text = await profile_actions.get_top_users()
    await message.answer(top_text, parse_mode=ParseMode.HTML)


@user_private_router.message(Command("subscribe"))
async def subscribe_cmd(message: types.Message):
    subscribe_text = (
        "Подписка на премиум открывает доступ к следующим функциям:\n"
        "• Увеличенный лимит на создание целей\n"
        "• Доступ к уникальным вызовам\n"
        "• Расширенные возможности мониторинга и отчётов\n"
        "• Специальные награды и достижения\n\n"
        "Для оформления подписки, перейдите по следующей ссылке: [Оформить подписку](https://example.com/pay)"
    )
    await message.answer(subscribe_text, parse_mode=ParseMode.MARKDOWN)


# Код ниже для машины состояний (FSM)


# обработчик для отмены всех состояний
# добавляем StateFilter('*'), где '*' - любое состояние пользователя
@user_private_router.message(StateFilter('*'), Command("отменить"))
@user_private_router.message(StateFilter('*'), F.text.lower() == "отменить")
async def cancel_handler(message: types.Message, state: FSMContext) -> None:
    # Получаем текущее состояние
    current_state = await state.get_state()

    # Если у пользователя нет состояния, то выходим из обработчика
    if current_state:
        # Очищаем все состояния пользователя
        await state.clear()

    # Отправляем сообщение об отмене и возвращаем начальную клавиатуру
    await send_message_with_keyboard(message, "Действия отменены", "user")


# Обработчик для кнопки "Бросить вызов"
@user_private_router.callback_query(lambda c: c.data == "challenge")
async def handle_challenge(callback_query: types.CallbackQuery, state: FSMContext):
    user_id = callback_query.from_user.id
    user_profile = global_vars.get_user_profile(user_id)

    # Проверка, является ли пользователь премиум
    if not user_profile.is_premium:
        await callback_query.message.answer(
            "Эта функция доступна только для премиум-пользователей. "
            "Оформите подписку с помощью команды /subscribe."
        )
        return

    # Если подписка активна, начинаем процесс вызова
    await callback_query.message.answer(
        "Выберите пользователя, которому хотите бросить вызов. Введите имя пользователя или ID.")
    await state.set_state(ChallengeStates.choose_opponent)


@user_private_router.message(ChallengeStates.choose_opponent)
async def choose_opponent(message: types.Message, state: FSMContext):
    opponent = message.text
    await state.update_data(opponent=opponent)
    await message.answer(f"Вы выбрали пользователя: {opponent}. Теперь введите условия для вызова.")
    await state.set_state(ChallengeStates.set_conditions)


@user_private_router.message(ChallengeStates.set_conditions)
async def set_conditions(message: types.Message, state: FSMContext):
    conditions = message.text
    await state.update_data(conditions=conditions)
    await message.answer(f"Условия вызова: {conditions}. Теперь установите ставку для вызова.")
    await state.set_state(ChallengeStates.set_bet)


@user_private_router.message(ChallengeStates.set_bet)
async def set_bet(message: types.Message, state: FSMContext):
    bet = message.text
    await state.update_data(bet=bet)
    await message.answer(f"Ставка установлена: {bet}. Укажите срок выполнения вызова (например, 7 дней).")
    await state.set_state(ChallengeStates.set_deadline)


@user_private_router.message(ChallengeStates.set_deadline)
async def set_deadline(message: types.Message, state: FSMContext):
    deadline = message.text
    data = await state.get_data()

    # Сохраняем данные вызова
    opponent = data.get("opponent")
    conditions = data.get("conditions")
    bet = data.get("bet")

    await message.answer(
        f"Вызов создан!\n"
        f"Противник: {opponent}\n"
        f"Условия: {conditions}\n"
        f"Ставка: {bet}\n"
        f"Срок: {deadline}"
    )

    # Очистка состояния
    await state.clear()
