from sqlalchemy.orm.session import Session
from db.schemas import processingBase, processingDisplay
from db.models import dbProcessing

def new_facilities(db: Session, request: processingBase):
    new_facilities = dbProcessing(
        processing_name = request.processing_name,
        processing_address = request.processing_address,
        processing_product = request.processing_product,
        processing_date = request.processing_date
    )
    db.add(new_facilities)
    db.commit()
    db.refresh(new_facilities)
    return new_facilities

# Update name by id
def update_name (db: Session, id: int, new_name: str):
    facilities = db.query(dbProcessing).filter(dbProcessing.id == id).first()
    facilities.processing_name = new_name
    db.commit()
    db.refresh(facilities)
    return facilities
    
# Update address by id 
def update_address (db: Session, id: int, new_address: str):
    facilities = db.query(dbProcessing).filter(dbProcessing.id == id).first()
    facilities.processing_address = new_address
    db.commit()
    db.refresh(facilities)
    return facilities

# Update product by id 
def update_product (db: Session, id: int, new_product: str):
    facilities = db.query(dbProcessing).filter(dbProcessing.id == id).first()
    facilities.processing_product = new_product
    db.commit()
    db.refresh(facilities)
    return facilities

# Update date by id
def update_date (db: Session, id: int, new_date: str):
    facilities = db.query(dbProcessing).filter(dbProcessing.id == id).first()
    facilities.processing_date = new_date
    db.commit()
    db.refresh(facilities)
    return facilities

