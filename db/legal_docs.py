from sqlalchemy.orm.session import Session
from db.schemas import documentBase, documentDisplay
from db.models import dbLegal

def new_legal_doc ( db: Session, request: documentBase):
    new_doc = dbLegal(
        title = request.title,
        file = request.file,
        issue_date = request.issue_date
    )
    db.add(new_doc)
    db.commit()
    db.refresh(new_doc)
    return new_doc
# UPdate title
def update_title (db: Session, id: int, new_title: str):
    titled = db.query(dbLegal).filter(dbLegal.id == id).first()
    titled.title = new_title
    db.commit()
    db.refresh(titled)
    return titled
# Update file
def update_file (db: Session, id: int, new_file: str):
    new = db.query(dbLegal).filter(dbLegal.id == id).first()
    new.file = new_file
    db.commit()
    db.refresh(new)
    return new
#Update date
def update_date ( db: Session, id: int, new_date: str):
    new = db.query(dbLegal).filter(dbLegal.id == id).first()
    new.issue_date = new_date
    db.commit()
    db.refresh(new)
    return new