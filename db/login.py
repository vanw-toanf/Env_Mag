from datetime import datetime
from sqlalchemy.orm.session import Session
from db.models import dbLoginHistory

def save_login_history(db: Session, user_id: int, ip_address: str):
    login_history_entry = dbLoginHistory(
        user_id=user_id,
        login_time=datetime.now(),
        ip_address=ip_address
    )
    db.add(login_history_entry)
    db.commit()
    db.refresh(login_history_entry)
    return login_history_entry
def get_login_history(db: Session, user_id: int):
    return db.query(dbLoginHistory).filter(dbLoginHistory.user_id == user_id).all()
def get_all_login_history(db: Session):
    return db.query(dbLoginHistory).all()