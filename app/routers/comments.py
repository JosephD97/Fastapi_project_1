from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, database, dependencies

router = APIRouter(prefix="/comments", tags=["comments"])

@router.post("/", response_model=schemas.CommentCreate)
def create_comment(
    comment: schemas.CommentCreate,
    db: Session = Depends(database.get_db),
    user_id: int = Depends(dependencies.get_current_user)
):
    return crud.create_comment(db, comment, user_id)

@router.put("/{comment_id}")
def update_comment(comment_id: int, comment: schemas.CommentUpdate, db: Session = Depends(database.get_db), user_id: int = Depends(dependencies.get_current_user)):
    db_comment = crud.get_comment(db, comment_id)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    if db_comment.owner_id != user_id:
        raise HTTPException(status_code=403, detail="Not allowed")
    return crud.update_comment(db, db_comment, comment)

@router.delete("/{comment_id}")
def delete_comment(comment_id: int, db: Session = Depends(database.get_db), user_id: int = Depends(dependencies.get_current_user)):
    db_comment = crud.get_comment(db, comment_id)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Сomment not found")
    if db_comment.owner_id != user_id:
        raise HTTPException(status_code=403, detail="Not allowed")
    return crud.delete_comment(db, db_comment)
