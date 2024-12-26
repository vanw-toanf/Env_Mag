from fastapi import APIRouter, Depends
from db.schemas import UserBase, GroupDisplay, GroupBase
from sqlalchemy.orm import Session
from db.database import get_db
from db import crud
router = APIRouter(
    prefix="/create_group",
    tags=["create_group"]
)
@router.post("/new_group", response_model=GroupDisplay)
def create_group(request: GroupBase, db: Session=Depends(get_db)):
    return crud.create_group(db, request)
@router.post("/delete_all_group")
def delete_all_group(db: Session=Depends(get_db)):
    return crud.delete_all_group(db)