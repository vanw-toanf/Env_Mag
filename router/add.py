from fastapi import APIRouter, Depends
from db.schemas import UserBase, RoleDisplay, LFBase, LFDisplay, constructionBase, constructionDisplay, Condition, ConditionShow, HanhChinhBase, HanhChinhDisplay
from db.schemas import processingBase, processingDisplay, HanhChinhBase, HanhChinhDisplay, documentBase, documentDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db import guest_permission, admin_permission, huyen_xa_moi
from db import livestock, construction, product, legal_docs


router = APIRouter(
    prefix="/add",
    tags=["add"]
)
# Huyen,xa
@router.post("/add_huyen", response_model = HanhChinhDisplay)
def add_huyen (request: HanhChinhBase, db: Session=Depends(get_db)):
    return huyen_xa_moi.huyen(db,request)
@router.post("/add_xa", response_model = HanhChinhDisplay)
def add_xa (request: HanhChinhBase, db: Session = Depends(get_db)):
    return huyen_xa_moi.xa(db,request)

@router.post("/add_guest_role", response_model=RoleDisplay)
def add_guest_role(db: Session=Depends(get_db)):
    return guest_permission.create_guest_role(db)
@router.post("/add_admin_role", response_model=RoleDisplay)
def add_admin_role(db: Session=Depends(get_db)):
    return admin_permission.create_admin_role(db)

#Livestock
@router.post("/add_LF", response_model=LFDisplay)
def add_LF(request: LFBase, db: Session=Depends(get_db)):
    return livestock.add_LF(db, request)
@router.post("/add_staff_for_LF", response_model= LFDisplay)
def add_staff(request: LFBase, farm_id: int, db: Session=Depends(get_db)):
    return livestock.add_staff(db, request, farm_id)
@router.post("/add_condition_for_LF", response_model= ConditionShow)
def add_condition(request: Condition, farm_id: int, db: Session=Depends(get_db)):
    return livestock.add_condition(db, request, farm_id)
#Construction    
@router.post("/add_waterFocus", response_model= constructionDisplay)
def add_construction(request: constructionBase, db: Session=Depends(get_db)):
    return construction.new_water_focus(db, request)
@router.post("/add_waterRetail", response_model= constructionDisplay)
def add_construction(request: constructionBase, db: Session=Depends(get_db)):
    return construction.new_water_retail(db, request)
#Processing
@router.post("/add_processing_facilities", response_model=processingDisplay)
def add_processing_facilities(request: processingBase, db: Session=Depends(get_db)):
    return product.new_facilities(db, request)

# Legal document
@router.post("/add_docs", response_model = documentDisplay)
def add_legal_doc (request: documentBase, db: Session=Depends(get_db)):
    return legal_docs.new_legal_doc(db, request)