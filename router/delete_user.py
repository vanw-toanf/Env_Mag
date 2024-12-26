from fastapi import APIRouter, Depends
from db.schemas import UserBase, UserDisplay, DeleteDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db import crud

router = APIRouter(
    prefix="/delete_user", # prefix la duong dan truoc moi duong dan con
    tags=["delete_user"] # tags la ten cua router
)
@router.post("/delete_user", response_model = DeleteDisplay)
# delete user by username
def delete_user(request: UserBase, db: Session=Depends(get_db)):
    return crud.delete_user(db=db, request=request)
