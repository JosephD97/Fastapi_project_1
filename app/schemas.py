from pydantic import BaseModel, EmailStr
from datetime import datetime

# Общие поля пользователя
class UserBase(BaseModel):
    email:EmailStr

# Схема для создания пользователя
class UserCreate(UserBase):
    password: str

# Схема для отображения пользователя (без пароля)
class UserRead(UserBase):
    id:int
    created_at:datetime

    # чтобы Pydantic мог работать с объектами SQLAlchemy
    class Config:
        orm_mode=True

class UserLogin(BaseModel):
    email: str
    password: str