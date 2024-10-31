# reminders.py
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Bot
import datetime


# Функция для отправки напоминания о ежедневных задачах
async def send_daily_reminder(bot: Bot, user_id: str):
    await bot.send_message(user_id, "Не забудьте выполнить свои ежедневные задачи!")


# Функция для отправки напоминания об окончании срока вызова
async def send_challenge_reminder(bot: Bot, user_id: str, days_left: int):
    await bot.send_message(user_id, f"Напоминание: до окончания вашего вызова осталось {days_left} дней!")


# Функция для отправки еженедельного отчета
async def send_weekly_report_reminder(bot: Bot, user_id: str):
    await bot.send_message(user_id, "Напоминаем, что ваши еженедельные задачи нужно завершить завтра!")


# Функция для инициализации планировщика
def start_scheduler(bot: Bot):
    scheduler = AsyncIOScheduler()

    # Примерные задачи напоминаний для ежедневных задач
    scheduler.add_job(send_daily_reminder, "cron", hour=9, args=[bot, "dyakart"])  # Укажите реальные user_id
    scheduler.add_job(send_daily_reminder, "cron", hour=15, args=[bot, "dyakart"])
    scheduler.add_job(send_daily_reminder, "cron", hour=21, args=[bot, "dyakart"])

    # Пример задачи для напоминания об окончании срока вызова
    scheduler.add_job(send_challenge_reminder, "interval", days=1, args=[bot, "dyakart", 3])  # 3 дня до конца вызова

    # Пример задачи для напоминания об окончании еженедельных задач
    scheduler.add_job(send_weekly_report_reminder, "cron", day_of_week="sun", hour=18, args=[bot, "dyakart"])

    # Запуск планировщика
    scheduler.start()
