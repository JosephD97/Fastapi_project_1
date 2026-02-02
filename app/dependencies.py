from .database import SessionLocal

# Dependency
def get_db():
    db=SessionLocal() # SessionLocal() создаёт новую сессию SQLAlchemy
    try:
        yield db # yield отдаёт её FastAPI endpoint
    finally: # SПосле выполнения запроса сессия закрывается автоматически (finally)
        db.close()