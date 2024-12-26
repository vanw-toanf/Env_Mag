from fastapi import APIRouter, HTTPException, Depends
from db.schemas import UserBase, UserDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db import crud


router = APIRouter(
    prefix="/register_user",
    tags=["register_user"]
)

@router.post("/new_user")
async def register_user(request: UserBase, db: Session = Depends(get_db)):
    try:
        return crud.create_user(db, request, role_name="User")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/new_admin")
async def create_admin(request: UserBase, db: Session=Depends(get_db)):
    try:
        return crud.create_admin(db, request, role_name="Admin")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

