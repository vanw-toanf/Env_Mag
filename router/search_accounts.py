from fastapi import APIRouter, Depends, HTTPException, status
from db.schemas import UserBase, UserDisplay, DeleteDisplay, GroupBase, GroupDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db import admin_permission
from pydantic import BaseModel

router = APIRouter(
    prefix="/search",
    tags=["search"]
)

# Định nghĩa Pydantic model cho tìm kiếm người dùng
class SearchRequest(BaseModel):
    find_id: int

@router.get("/all/", response_model=list[UserDisplay])
async def get_all_users(db: Session = Depends(get_db)):
    """
    Lấy tất cả người dùng từ cơ sở dữ liệu.
    Sử dụng phương thức GET thay vì POST.
    """
    try:
        users = admin_permission.get_all(db=db)  # Loại bỏ tham số 'request' nếu không cần thiết
        return [UserDisplay.from_orm(user) for user in users]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# @router.get("/person/", response_model=UserDisplay)
# async def search_guest(request: SearchRequest, db: Session = Depends(get_db)):
#     try:
#         user = admin_permission.search_guest_accounts(db=db, find_id=request.find_id)
#         if not user:
#             raise HTTPException(status_code=404, detail="User not found")
#         return UserDisplay.from_orm(user)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

@router.get("/group/", response_model=list[GroupDisplay])
async def all_groups(db: Session = Depends(get_db)):
    try:
        groups = admin_permission.get_all_group(db=db)
        return [GroupDisplay.from_orm(group) for group in groups]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/user/{username}", response_model=UserDisplay)
async def search_user(username: str, db: Session = Depends(get_db)):
    """
    Tìm kiếm người dùng theo username.
    """
    try:
        user = admin_permission.search_guest_accounts(db=db, find_name=username).all()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return UserDisplay.from_orm(user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))