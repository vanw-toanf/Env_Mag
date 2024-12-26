from fastapi import APIRouter, Depends
from db.schemas import UserBase, UserDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db import admin_permission
from typing import List

router = APIRouter(
    prefix="/statistic_user",
    tags=["statistic_user"]
)
@router.post("/list_user", response_model=List[UserDisplay])
# List all users in the database
def list_all_users(request: UserBase, db: Session=Depends(get_db)):
    return list_user.get_all(db=db, request=request)
