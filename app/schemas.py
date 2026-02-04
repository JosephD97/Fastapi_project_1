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





class PostCreate(BaseModel):
    title: str
    content: str

class PostUpdate(BaseModel):
    title: str
    content: str

class CommentCreate(BaseModel):
    text: str

class CommentUpdate(BaseModel):
    text: str

class CommentRead(BaseModel):
    id: int
    text: str
    owner_id: int
    post_id: int

    class Config:
        orm_mode = True