from sqlalchemy.orm import Session
from . import models, schemas
# CRUD = Create, Read, Update, Delete


# функция для создания нового пользователя
def create_user(db: Session, user: schemas.UserCreate):
    # создаём объект модели User, заполняем email и пароль
    # user - это Pydantic схема (UserCreate) с данными от клиента
    db_user = models.User(
        email=user.email,
        hashed_password=user.hashed_password
    )
    db.add(db_user)       # добавляем объект в сессию (пока не в БД, только в память)
    db.commit()           # сохраняем изменения в базе данных (создаём запись)
    db.refresh(db_user)   # обновляем объект db_user данными из БД (например, чтобы получить id)
    return db_user        # возвращаем объект пользователя

# получить пользователя по email
def get_user_by_email(db: Session, email: str):
    # создаём запрос к таблице users, фильтруем по email, возвращаем первый результат
    return db.query(models.User).filter(models.User.email == email).first()

# получить пользователя по id
def get_user(db: Session, user_id: int):
    # создаём запрос к таблице users, фильтруем по id, возвращаем первый результат
    return db.query(models.User).filter(models.User.id == user_id).first()

# получить всех пользователей (опционально с лимитом)
def get_users(db: Session, skip: int = 0, limit: int = 100):
    # запрашиваем всех пользователей, пропускаем первые `skip`, ограничиваем `limit`
    return db.query(models.User).offset(skip).limit(limit).all()