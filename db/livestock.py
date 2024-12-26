from sqlalchemy.orm.session import Session
from sqlalchemy import join
from db.schemas import LFBase, LFDisplay
from db.models import dbFarm, dbFarmStaff, dbCondition

# New livestock facility
def add_LF (db: Session, request: LFBase):
    new_LF = dbFarm(
        name = request.name,
        owner = request.owner,
        register_date = request.register_date
    )
    db.add(new_LF)
    db.commit()
    db.refresh(new_LF)
    return new_LF
def add_staff (db: Session, request: LFBase, farm_id: int):
    new_staff = dbFarmStaff(
        staff_name = request.owner,
        farm_id = farm_id
    )
    db.add(new_staff)
    db.commit()
    db.refresh(new_staff)
    return new_staff
def add_condition (db: Session, request: LFBase, farm_id: int, conditions: str):
    new_condition = dbCondition(
        farm_id = farm_id,
        condition = conditions,
    )
    db.add(new_condition)
    db.commit()
    db.refresh(new_condition)
    return new_condition
# Delete in4
def delete_LF (db: Session, farm_id: int):
    db.query(dbFarm).filter(dbFarm.id == farm_id).delete()
    db.commit()
    return {"message": "Delete successfully"}
def delete_staff (db: Session, staff_id: int):
    db.query(dbFarmStaff).filter(dbFarmStaff.id == staff_id).delete()
    db.commit()
    return {"message": "Delete successfully"}
def delete_condition (db: Session, condition_id: int):
    db.query(dbCondition).filter(dbCondition.id == condition_id).delete()
    db.commit()
    return {"message": "Delete successfully"}
# join dbFarm and dbCondition
def get_farm_with_condition (db: Session):
    results = db.query(
        dbFarm.id.label("farm_id"),
        dbFarm.name,
        dbFarm.owner,
        dbFarm.register_date,
        dbCondition.condition
    ).join(dbCondition, dbFarm.id == dbCondition.farm_id).all()
    return results
# List all farm
def get_all_farm (db: Session):
    return db.query(dbFarm).all()
# Find farm by id
def get_farm_by_id (db: Session, farm_id: int):
    return db.query(dbFarm).filter(dbFarm.id == farm_id).first()