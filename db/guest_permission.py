from sqlalchemy.orm.session import Session
from db.schemas import UserBase, UserUpdate
from db.models import dbUser, dbRole, dbPermission
from db.hash import Hash

def create_guest_role(db: Session):
    existing_role = db.query(dbRole).filter(dbRole.name == "guest").first()
    if existing_role:
        return existing_role  # the role has already exists

    guest_role = dbRole(
        name="guest",
        description="Guest users with limited access to personal account settings."
    )
    db.add(guest_role)
    db.commit()
    db.refresh(guest_role)  
    
    guest_permissions = [
        dbPermission(role_id=guest_role.id, permission_name="modify_own_account")
    ]
    db.add_all(guest_permissions) # add all permissions to the database
    db.commit()
    return guest_role

# Guest only able to update their own information
def edit_password ( db: Session, user_id: int, present_password: str, new_password: str):
    user = db.query(dbUser).filter(dbUser.id == user_id).first()
    # check if the user input the correct present password --> if not return error
    if not Hash.verify(user.password, present_password):
        return {"error": "Present password is incorrect"}
    else:
        user.password = Hash.bcrypt(new_password)
        db.commit()
        db.refresh(user)
        return user
def edit_user (db: Session, user_id: int, request: UserUpdate):
    user = db.query(dbUser).filter(dbUser.id == user_id).first()
    if request.fullname:
        user.fullname = request.fullname
    if request.username:
        user.username = request.username
    if request.email:
        user.email = request.email
    db.commit()
    db.refresh(user)
    return user