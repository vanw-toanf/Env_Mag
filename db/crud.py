from sqlalchemy.orm.session import Session
from db.schemas import UserBase, GroupBase
from db.models import dbUser, dbRole, dbUserGroup, dbGroup_Member
from db.hash import Hash


def create_user(db: Session, request: UserBase, group_id: int = None, role_name: str = "guest"): 
    role = db.query(dbRole).filter(dbRole.name == role_name).first()
    if not role:
        return {"error": "Role '{role_name}' not found"}
    new_user = dbUser(
        fullname=request.fullname,
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password),
        role_id=role.id,
        status=True  # Mặc định người dùng hoạt động
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    # Check if the user needs to be assigned to a group
    if group_id:
        # Verify if the group exists by querying dbUserGroup (optional)
        group = db.query(dbUserGroup).filter(dbUserGroup.id == group_id).first()
        if not group:
            return {"error": "Group not found"}
        # Check if the user is already in the group
        group_member = db.query(dbGroup_Member).filter(
            dbGroup_Member.user_id == new_user.id,
            dbGroup_Member.group_id == group_id
        ).first()
        if not group_member:
            # Add user to group since they are not yet a member
            new_group_member = dbGroup_Member(user_id=new_user.id, group_id=group_id)
            db.add(new_group_member)
            db.commit()
            db.refresh(new_group_member)
            return new_user
    return {"user": new_user, "group_membership": "None"}
    # return new_user

def delete_user(db: Session, user_id: int): # Delete user by user_id
    user = db.query(dbUser).filter(dbUser.id == user_id).first()
    db.delete(user)
    db.commit()
    db.refresh(user)
    return user

# Create new group for dbUserGroup
def create_group(db: Session, request: GroupBase):
    new_group = dbUserGroup(
        group_name = request.group_name,
        description = request.description
    )
    db.add(new_group)
    db.commit()
    db.refresh(new_group)
    return new_group

#Delete all group 
def delete_all_group(db: Session):
    group = db.query(dbUserGroup).all()
    for i in group:
        db.delete(i)
    db.commit()
    return group

# Create new admin
def create_admin(db: Session, request: UserBase, role_name: str = "Admin"):
    role = db.query(dbRole).filter(dbRole.name == role_name).first()
    if not role:
        return {"error": "Role '{role_name}' not found"}
    new_user = dbUser(
        fullname=request.fullname,
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password),
        role_id=role.id,
        status=True  # Mặc định người dùng hoạt động
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user