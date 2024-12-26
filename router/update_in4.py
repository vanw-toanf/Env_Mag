from fastapi import APIRouter, Depends
from db.schemas import UserBase, RoleDisplay, LFBase, LFDisplay, constructionBase, constructionDisplay
from db.schemas import processingBase, processingDisplay, documentBase, documentDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db import guest_permission, admin_permission
from db import livestock, construction, product, huyen_xa_moi
router = APIRouter(
    prefix="/update",
    tags=["update"]
)
#LF
@router.post("delete_LF", response_model=LFDisplay)
def delete_LF(farm_id: int, db: Session=Depends(get_db)):
    return livestock.delete_LF(db, farm_id)
@router.post("delete_staff", response_model=LFDisplay)
def delete_staff(staff_id: int, db: Session=Depends(get_db)):
    return livestock.delete_staff(db, staff_id)
@router.post("delete_condition", response_model=LFDisplay)
def delete_condition(condition_id: int, db: Session=Depends(get_db)):
    return livestock.delete_condition(db, condition_id) 

#Construction
@router.post("update_focus_name", response_model=constructionDisplay)
def update_focus_name(id: int, new_name: str, db: Session=Depends(get_db)):
    return construction.update_focus_name(db, id, new_name)
@router.post("update_retail_name", response_model=constructionDisplay)
def update_retail_name(id: int, new_name: str, db: Session=Depends(get_db)):
    return construction.update_retail_name(db, id, new_name)

@router.post("update_focus_location", response_model=constructionDisplay)
def update_focus_location(id: int, new_location: str, db: Session=Depends(get_db)):
    return construction.update_focus_location(db, id, new_location)
@router.post("update_retail_location", response_model=constructionDisplay)
def update_retail_location(id: int, new_location: str, db: Session=Depends(get_db)):
    return construction.update_retail_location(db, id, new_location)

@router.post("update_focus_status", response_model=constructionDisplay)
def update_focus_status(id: int, new_status: str, db: Session=Depends(get_db)):
    return construction.update_focus_status(db, id, new_status)
@router.post("update_retail_status", response_model=constructionDisplay)
def update_retail_status(id: int, new_status: str, db: Session=Depends(get_db)):
    return construction.update_retail_status(db, id, new_status)

@router.post("update_focus_chi_so_nuoc", response_model=constructionDisplay)
def update_focus_chi_so_nuoc(id: int, new_chi_so_nuoc: str, db: Session=Depends(get_db)):
    return construction.update_focus_chi_so_nuoc(db, id, new_chi_so_nuoc)
@router.post("update_retail_chi_so_nuoc", response_model=constructionDisplay)
def update_retail_chi_so_nuoc(id: int, new_chi_so_nuoc: str, db: Session=Depends(get_db)):
    return construction.update_retail_chi_so_nuoc(db, id, new_chi_so_nuoc)

#Processing
@router.post("update_processing_name", response_model=processingDisplay)
def update_processing_name(id: int, new_name: str, db: Session=Depends(get_db)):
    return product.update_processing_name(db, id, new_name)
@router.post("update_processing_address", response_model=processingDisplay)
def update_processing_address(id: int, new_address: str, db: Session=Depends(get_db)):
    return product.update_processing_address(db, id, new_address)
@router.post("update_processing_product", response_model=processingDisplay)
def update_processing_product(id: int, new_product: str, db: Session=Depends(get_db)):
    return product.update_processing_product(db, id, new_product)
@router.post("update_processing_date", response_model=processingDisplay)
def update_processing_date(id: int, new_date: str, db: Session=Depends(get_db)):
    return product.update_processing_date(db, id, new_date)

#Legal document
@router.post("update_title", response_model=documentDisplay)
def update_title(id: int, new_title: str, db: Session=Depends(get_db)):
    return legal_docs.update_title(db, id, new_title)
@router.post("update_file", response_model=documentDisplay)
def update_file(id: int, new_file: str, db: Session=Depends(get_db)):
    return legal_docs.update_file(db, id, new_file)
@router.post("update_date", response_model=documentDisplay)
def update_date(id: int, new_date: str, db: Session=Depends(get_db)):
    return legal_docs.update_date(db, id, new_date)