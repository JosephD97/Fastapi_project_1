from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, database, dependencies

router = APIRouter(prefix="/posts", tags=["posts"])

@router.post("/", response_model=schemas.PostCreate)
def create_post(post: schemas.PostCreate, db: Session = Depends(database.get_db), user_id: int = Depends(dependencies.get_current_user)):
    return crud.create_post(db, post, user_id)

@router.put("/{post_id}")
def update_post(post_id: int, post: schemas.PostUpdate, db: Session = Depends(database.get_db), user_id: int = Depends(dependencies.get_current_user)):
    db_post = crud.get_post(db, post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    if db_post.owner_id != user_id:
        raise HTTPException(status_code=403, detail="Not allowed")
    return crud.update_post(db, db_post, post)

@router.delete("/{post_id}")
def delete_post(post_id: int, db: Session = Depends(database.get_db), user_id: int = Depends(dependencies.get_current_user)):
    db_post = crud.get_post(db, post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    if db_post.owner_id != user_id:
        raise HTTPException(status_code=403, detail="Not allowed")
    return crud.delete_post(db, db_post)
