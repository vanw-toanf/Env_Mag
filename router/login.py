from fastapi import APIRouter, HTTPException, Depends
from db.schemas import LoginRequest, LogoutRequest
from sqlalchemy.orm import Session
from db.database import get_db
from db.hash import Hash
from db import models
from datetime import datetime

router = APIRouter(
    prefix="/login",
    tags=["login"]
)

@router.post("/verify/")
async def login(data: LoginRequest, db: Session = Depends(get_db)):
    # Tìm người dùng dựa trên tên đăng nhập
    user = db.query(models.dbUser).filter(models.dbUser.username == data.username).first()

    # Kiểm tra nếu người dùng không tồn tại
    if not user or user.role_id != data.role_id:
        raise HTTPException(status_code=404, detail="User not found")

    # Kiểm tra mật khẩu
    if not Hash.verify(data.password, user.password):
        raise HTTPException(status_code=400, detail="Incorrect password")
    
    activity = db.query(models.dbUserActivity).filter(models.dbUserActivity.user_id == user.id).first()
    
    if activity:
        activity.IsActive = True
    else:
        new_activity = models.dbUserActivity(
            user_id = user.id,
            IsActive = True,
            LastActivity = datetime.utcnow()
        )
        db.add(new_activity)
    db.commit()
    return {"message": "Login successful"}

# Phải tạo router để chỉnh sửa dbUserActivity trong database
@router.post("/logout/") 
async def logout (data: LogoutRequest, db: Session = Depends(get_db)):
    user = db.query(models.dbUser).filter(models.dbUser.username == data.username,models.dbUser.role_id == data.role_id).first()
    # Kiểm tra nếu người dùng không tồn tại
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    activity = db.query(models.dbUserActivity).filter(models.dbUserActivity.user_id == user.user_id).first()
    if activity:
        activity.IsActive = False
        activity.LastActivity = datetime.utcnow()
        db.commit()
        return {"message": "Logged out successful"}
    else:
        raise HTTPException(status_code=404, detail="User activity not found")

