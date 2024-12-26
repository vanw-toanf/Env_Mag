from sqlalchemy.orm.session import Session
from db.schemas import constructionBase, constructionDisplay
from db.models import dbHuyen, dbXa, dbWaterFocus, dbWaterRetail, dbWaterReport, dbWaterStatistic

def new_water_focus(db: Session, request: constructionBase):
    # status_boolean = True if request.status == '1' else False
    new_focus = dbWaterFocus(
        name = request.name,
        location = request.location,
        status = request.status,
        construction_year = request.construction_year,
        chi_so_nuoc = request.chi_so_nuoc
    )
    db.add(new_focus)
    db.commit()
    db.refresh(new_focus)
    return new_focus
def new_water_retail(db: Session, request: constructionBase):
    # Chuyển status từ string sang boolean
    # status_boolean = True if request.status == '1' else False
    new_retail = dbWaterRetail(
        name = request.name,
        location = request.location,
        status = request.status,
        construction_year = request.construction_year,
        chi_so_nuoc = request.chi_so_nuoc
    )
    db.add(new_retail)
    db.commit()
    db.refresh(new_retail)
    return new_retail
# Update name
def update_focus_name(db: Session, id: int, new_name: str):
    focus = db.query(dbWaterFocus).filter(dbWaterFocus.id == id).first()
    focus.focus_name = new_name
    db.commit()
    db.refresh(focus)
    return focus
def update_retail_name(db: Session, new_name: str, id: int):
    retail = db.query(dbWaterRetail).filter(dbWaterRetail.id == id).first()
    retail.retail_name = new_name
    db.commit()
    db.refresh(retail)
    return retail
# Update location
def update_focus_location(db: Session, new_location: str, id: int):
    focus = db.query(dbWaterFocus).filter(dbWaterFocus.id == id).first()
    focus.location = new_location
    db.commit()
    db.refresh(focus)
    return focus
def update_retail_location(db: Session, new_location: str, id: int):
    retail = db.query(dbWaterRetail).filter(dbWaterRetail.id == id).first()
    retail.location = new_location
    db.commit()
    db.refresh(retail)
    return retail
# Update status
def update_focus_status(db: Session, new_status: str, id: int):
    focus = db.query(dbWaterFocus).filter(dbWaterFocus.id == id).first()
    focus.status = new_status
    db.commit()
    db.refresh(focus)
    return focus
def update_retail_status(db: Session, new_status: str, id: int):
    retail = db.query(dbWaterRetail).filter(dbWaterRetail.id == id).first()
    retail.status = new_status
    db.commit()
    db.refresh(retail)
    return retail
# Update chi_so_nuoc
def update_focus_chi_so_nuoc(db: Session, new_chi_so_nuoc: str, id: int):
    focus = db.query(dbWaterFocus).filter(dbWaterFocus.id == id).first()
    focus.chi_so_nuoc = new_chi_so_nuoc
    db.commit()
    db.refresh(focus)
    return focus
def update_retail_chi_so_nuoc(db: Session, new_chi_so_nuoc: str, id: int):
    retail = db.query(dbWaterRetail).filter(dbWaterRetail.id == id).first()
    retail.chi_so_nuoc = new_chi_so_nuoc
    db.commit()
    db.refresh(retail)
    return retail
# List construction base on xa_id
def find_focus_construction (db: Session, id: int):
    return db.query(dbWaterFocus).filter(dbWaterFocus.id == id).all()
def find_retail_construction (db: Session, id: int):
    return db.query(dbWaterRetail).filter(dbWaterRetail.id == id).all()
# List all construction
def get_all_retail(db: Session):
    return db.query(dbWaterRetail).all()
def get_all_focus(db: Session):
    return db.query(dbWaterFocus).all()

