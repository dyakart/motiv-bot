# user_service.py
from sqlalchemy.orm import Session
from models import User

def get_user(db: Session, telegram_id: int):
    return db.query(User).filter(User.telegram_id == telegram_id).first()

def create_user(db: Session, telegram_id: int):
    db_user = User(telegram_id=telegram_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
