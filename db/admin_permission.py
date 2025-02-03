from sqlalchemy.orm.session import Session
from db.schemas import UserBase
from db.models import dbUser, dbRole, dbPermission, dbUserGroup, dbGroup_Member
from db.hash import Hash

def create_admin_role(db: Session):
    existing_role = db.query(dbRole).filter(dbRole.name == "admin").first()
    if existing_role:
        return existing_role  # the role has already exists

    admin_role = dbRole(
        name="admin",
        description="Admin users with full access to modify all accounts along with website settings and information."
    )
    db.add(admin_role)
    db.commit()
    db.refresh(admin_role)  
    
    admin_permissions = [
        dbPermission(role_id=admin_role.id, permission_name="check_login_history"),
        dbPermission(role_id=admin_role.id, permission_name="modify_website_info"),
        dbPermission(role_id=admin_role.id, permission_name="search_guest_accounts"),
        dbPermission(role_id=admin_role.id, permission_name="check_account_status"),
        dbPermission(role_id=admin_role.id, permission_name="view_statistics")
    ]
    db.add_all(admin_permissions) # add all permissions to the database
    db.commit()
    db.refresh(admin_role)
    return admin_role

# Find users and group_users
def search_guest_accounts(db: Session, find_name: str):
    # Return all information of user with id = find_id
    return db.query(dbUser).filter(dbUser.username == find_name).all()

def get_all(db: Session):
    return db.query(dbUser).all()

def get_all_group(db: Session):
    return db.query(dbUserGroup).all()

def get_group_member(db: Session, group_id: int):
    return db.query(dbGroup_Member).filter(dbGroup_Member.group_id == group_id).all()