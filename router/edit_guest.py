from fastapi import APIRouter, Depends
from db.schemas import UserBase, UserDisplay, DeleteDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db import guest_permission
router = APIRouter(
    prefix="/edit_own_account",
    tags=["edit_own_account"]
)
@router.post("/edit_user", response_model=UserDisplay)
def edit_user(user_id: int, request: UserBase, db: Session=Depends(get_db)):
    return guest_permission.edit_user(db=db, user_id=user_id, request=request)
@router.post("/edit_password", response_model=UserDisplay)
def edit_password(user_id: int, present_password: str, new_password: str, db: Session=Depends(get_db)):
    return guest_permission.edit_password(db=db, user_id=user_id, present_password=present_password, new_password=new_password)
