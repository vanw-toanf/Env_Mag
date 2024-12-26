from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional, List
from decimal import Decimal
# from sqlalchemy.sql.sqltypes import Integer, Date,TIMESTAMP, Boolean
from datetime import date

class HanhChinhBase (BaseModel):
    name: str
    code: str
class HanhChinhDisplay (BaseModel):
    name: str
    code: str
    class Config:
        from_attributes = True

class UserBase(BaseModel):
    fullname: str = Field(..., max_length=255)
    username: str = Field(..., max_length=25)
    password: str = Field(..., min_length=6)  # Yêu cầu mật khẩu tối thiểu 6 ký tự
    email: EmailStr

    class Config:
        from_attributes = True

class LoginRequest(BaseModel):
    username: str
    password: str
    role_id: int
class LogoutRequest(BaseModel):
    username: str
    role_id: int

class UserDisplay(BaseModel):
    id: int
    fullname: str
    username: str
    email: str
    role_id: int
    class Config():
        from_attributes = True

class DeleteDisplay(BaseModel):
    username: str
    class Config():
        from_attributes = True 
        # from_attributes = True la de chuyen tu camelCase sang snake_case

class UserUpdate(BaseModel):
    fullname: Optional[str]
    username: Optional[str]
    email: Optional[str]
    password: Optional[str]


class GroupBase(BaseModel):
    group_name: str
    description: str

class GroupDisplay(BaseModel):
    group_name: str
    description: str
    class Config():
        from_attributes = True


class RoleDisplay(BaseModel):
    name: str
    description: str
    class Config():
        from_attributes = True


# Livestock facility base
class LFBase(BaseModel):
    name: str
    owner: str
    register_date: str

class LFDisplay(BaseModel):
    name: str
    owner: str
    register_date: str
    class Config():
        from_attributes = True 
# livestock farm join with condition display
class ConditionDisplay(BaseModel):
    farm_id: int
    name: str
    owner: str
    register_date: Optional[str]  # Trả về dưới dạng chuỗi
    condition: str

    class Config:
        from_attributes = True

    @validator("register_date", pre=True, always=True)
    def format_register_date(cls, value):
        if value and isinstance(value, date):
            return value.strftime("%d-%m-%Y")  # Định dạng thành chuỗi YYYY-MM-DD
        return None

# Construction base
class constructionBase(BaseModel):
    name: str
    location: str
    status: str
    construction_year: str
    chi_so_nuoc: Decimal
    
class constructionDisplay(BaseModel):
    id: int
    name: str
    location: str
    status: str
    construction_year: str
    chi_so_nuoc: Decimal
    class Config():
        from_attributes = True

# Processing base
class processingBase(BaseModel):
    processing_name: str
    processing_address: str
    processing_product: str
    processing_date: str
class processingDisplay(BaseModel):
    processing_name: str
    processing_address: str
    processing_product: str
    processing_date: str
    class Config():
        from_attributes = True
# Legal documents
class documentBase(BaseModel):
    title: str
    file: str
    issue_date: str
class documentDisplay(BaseModel):
    title: str
    file: str
    issue_date: str
    class Config():
        from_attributes = True
# History access display
class statusDisplay(BaseModel):
    user_id: int
    IsActive: bool
    LastActivity: str
    class Config():
        from_attributes = True
