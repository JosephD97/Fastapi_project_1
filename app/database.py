from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import settings


DATABASE_URL = "postgresql://blog_user:123456@localhost:5432/blog_db"

# создаём соединение с базой
engine = create_engine(settings.DATABASE_URL)

# сессии для работы с БД
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# базовый класс для всех моделей
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()















'''
SELECT usename FROM pg_user - Запрос для списка пользователей
DROP USER имя_пользователя - Команда для удаления пользователя
REASSIGN OWNED BY blog_user TO postgres - передаёт объекты другому пользователю
CREATE USER blog_user WITH PASSWORD '123456' - Создаём пользователя
	blog_user — имя пользователя для проекта
	123456 — пароль (можно заменить на свой)
GRANT ALL PRIVILEGES ON DATABASE blog_db TO blog_user - Даем права на базу blog_db
'''