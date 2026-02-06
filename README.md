# FastAPI Blog API

REST API на FastAPI для работы с пользователями, постами и комментариями.  
Учебный проект.

## Tech stack

- Python
- FastAPI
- SQLAlchemy
- Alembic
- JWT

## Run project

```bash
git clone https://github.com/JosephD97/Fastapi_project_1.git
cd Fastapi_project_1

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
alembic upgrade head
uvicorn app.main:app --reload
