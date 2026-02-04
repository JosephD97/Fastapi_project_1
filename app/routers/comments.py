from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, database, dependencies

router = APIRouter(
    prefix="/posts/{post_id}/comments",
    tags=["comments"]
)


@router.post("/", response_model=schemas.CommentRead)
def create_comment(
    post_id: int,
    comment: schemas.CommentCreate,
    db: Session = Depends(database.get_db),
    user_id: int = Depends(dependencies.get_current_user)
):
    return crud.create_comment(db, comment, post_id, user_id)


@router.put("/{comment_id}", response_model=schemas.CommentRead)
def update_comment(
    post_id: int,
    comment_id: int,
    comment: schemas.CommentUpdate,
    db: Session = Depends(database.get_db),
    user_id: int = Depends(dependencies.get_current_user)
):
    db_comment = crud.get_comment(db, comment_id)
    if not db_comment or db_comment.post_id != post_id:
        raise HTTPException(status_code=404, detail="Comment not found")

    if db_comment.owner_id != user_id:
        raise HTTPException(status_code=403, detail="Not allowed")

    return crud.update_comment(db, db_comment, comment)


@router.delete("/{comment_id}")
def delete_comment(
    post_id: int,
    comment_id: int,
    db: Session = Depends(database.get_db),
    user_id: int = Depends(dependencies.get_current_user)
):
    db_comment = crud.get_comment(db, comment_id)
    if not db_comment or db_comment.post_id != post_id:
        raise HTTPException(status_code=404, detail="Comment not found")

    if db_comment.owner_id != user_id:
        raise HTTPException(status_code=403, detail="Not allowed")

    crud.delete_comment(db, db_comment)
    return {"detail": "Comment deleted"}

