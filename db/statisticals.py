from sqlalchemy.orm.session import Session
from db.schemas import statusDisplay
from db.models import dbUserActivity

#List all status
def list_status(db: Session):
    return db.query(dbUserActivity).all()
