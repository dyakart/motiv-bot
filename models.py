# models.py
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Float, Text
from sqlalchemy.orm import relationship
from database import Base


# Таблица пользователей
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(Integer, unique=True, index=True)
    is_premium = Column(Boolean, default=False)
    balance = Column(Float, default=0.0)
    rating = Column(Integer, default=0)
    health = Column(Integer, default=3)

    # Связи
    challenges = relationship("Challenge", back_populates="user")
    daily_tasks = relationship("DailyTask", back_populates="user")
    weekly_tasks = relationship("WeeklyTask", back_populates="user")
    custom_achievements = relationship("CustomAchievement", back_populates="user")
    wishes = relationship("Wish", back_populates="user")
    goals = relationship("Goal", back_populates="user")


# Таблица вызовов (спринтов)
class Challenge(Base):
    __tablename__ = "challenges"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    opponent_id = Column(Integer, ForeignKey("users.id"))
    description = Column(Text)
    bet = Column(Float, nullable=True)
    deadline = Column(DateTime)
    result = Column(String)

    # Связи
    user = relationship("User", foreign_keys=[user_id], back_populates="challenges")


# Таблица ежедневных задач
class DailyTask(Base):
    __tablename__ = "daily_tasks"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    description = Column(Text)
    completed = Column(Boolean, default=False)

    # Связи
    user = relationship("User", back_populates="daily_tasks")


# Таблица еженедельных задач
class WeeklyTask(Base):
    __tablename__ = "weekly_tasks"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    description = Column(Text)
    completed = Column(Boolean, default=False)
    deadline = Column(DateTime)

    # Связи
    user = relationship("User", back_populates="weekly_tasks")


# Таблица кастомных достижений
class CustomAchievement(Base):
    __tablename__ = "custom_achievements"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    description = Column(Text)
    completed = Column(Boolean, default=False)

    # Связи
    user = relationship("User", back_populates="custom_achievements")


# Таблица предустановленных достижений
class PredefinedAchievement(Base):
    __tablename__ = "predefined_achievements"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(Text)


# Таблица администраторов
class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(Integer, unique=True, index=True)


# Таблица для бан-листа
class BanList(Base):
    __tablename__ = "ban_list"

    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(Integer, unique=True, index=True)
    reason = Column(Text)


# Таблица желаний
class Wish(Base):
    __tablename__ = "wishes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    description = Column(Text)

    # Связи
    user = relationship("User", back_populates="wishes")


# Таблица целей
class Goal(Base):
    __tablename__ = "goals"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    description = Column(Text)
    deadline = Column(DateTime)

    # Связи
    user = relationship("User", back_populates="goals")
