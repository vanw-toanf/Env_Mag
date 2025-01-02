from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, TIMESTAMP, DECIMAL, Date, Numeric, DateTime
from db.database import Base
from datetime import datetime

"""
    Dinh nghia cac csdl
"""

## Bang quan ly nguoi dung
# Thong tin nguoi dung
class dbUser(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    fullname = Column(String(255))
    username = Column(String(25), unique=True)
    password = Column(String(72))
    email = Column(String(255))
    role_id = Column(Integer, ForeignKey('roles.id'))   # khoa ngoai tham chieu toi cot id cua bang roles

class dbUserActivity(Base):
    __tablename__ = 'user_activity'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    IsActive = Column(Boolean, default=False)
    LastActivity = Column(DateTime, default= datetime.utcnow)

# Dinh nghia cac quyen nguoi dung
class dbRole(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), unique=True)
    description = Column(String(255))        # mo ta quyen

# Phan quyen nguoi dung
class dbPermission(Base):
    __tablename__ = "permissions"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    role_id = Column(Integer, ForeignKey('roles.id'))
    permission_name = Column(String(255))        # ten quyen cu the

# Nhom nguoi dung
class dbUserGroup(Base):
    __tablename__ = "user_groups"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    group_name = Column(String(25))
    description = Column(String(255))        # mo ta nhom

# Thanh vien nhom
class dbGroup_Member(Base):
    __tablename__ = "user_group_members"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    group_id = Column(Integer, ForeignKey('user_groups.id'))

# Lich su dang nhap
class dbLoginHistory(Base):
    __tablename__ = "login_history"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    login_time = Column(TIMESTAMP)      # thoi gian dang nhap
    ip_address = Column(String(25))     # dia chi ip khi dang nhap


## Bang hanh chinh
# Cap huyen
class dbHuyen(Base):
    __tablename__ = "huyen"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(25))
    code = Column(String(25))

# Cap xa
class dbXa(Base):
    __tablename__ = "xa"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(25))
    code = Column(String(25))
    huyen_id = Column(Integer, ForeignKey('huyen.id'))


## Bang cong trinh nuoc sach
# Cong trinh nuoc sinh hoat tap trung
class dbWaterFocus(Base):
    __tablename__ = "cong_trinh_nuoc_tap_trung"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255))      # ten cong trinh
    location = Column(String(255))       # dia diem
    xa_id = Column(Integer, ForeignKey('xa.id'))
    status = Column(String(50))
    construction_year = Column(String(50))     # nam xay dung
    chi_so_nuoc = Column(DECIMAL)       # chi so nuoc

# Cong trinh nuoc sinh hoat nho le
class dbWaterRetail(Base):
    __tablename__ = "cong_trinh_nuoc_nho_le"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255))      # ten cong trinh
    location = Column(String(255))       # dia diem
    xa_id = Column(Integer, ForeignKey('xa.id')) 
    status = Column(String(50))
    construction_year = Column(String(50))     # nam xay dung
    chi_so_nuoc = Column(DECIMAL)      # chi so nuoc

# Bao cao quy hoach nuoc sach
class dbWaterReport(Base):
    __tablename__ = "water_report"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255))      # tieu de bao cao
    report_file = Column(String(255))        # duong dan file bao cao
    submit_date = Column(String(25))      # nagy nop bao cao


## Bang bao cao thong ke
# Thong ke cong trinh nuoc sach
class dbWaterStatistic(Base):
    __tablename__ = "water_statistic"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    cong_trinh_id = Column(Integer, ForeignKey('cong_trinh_nuoc_tap_trung.id'))
    date = Column(Date)     # ngay thong ke
    total_usage = Column(Numeric(6, 2))     # luong nuoc da cung cap

# So sanh cac cong trinh theo thoi gian
class dbCompare(Base):
    __tablename__ = "report_compare"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    cong_trinh_id = Column(Integer, ForeignKey('cong_trinh_nuoc_tap_trung.id'))
    time_period = Column(String(25))        # thoi gian so sanh (theo nam, quy)
    compare_result = Column(String(255))     # ket qua so sanh


## Bang chan nuoi
# Danh muc co so chan nuoi
class dbFarm(Base):
    __tablename__ = "farms"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255))       # ten co so chan nuoi
    owner = Column(String(255))      # ten chu so huu
    xa_id = Column(Integer, ForeignKey('xa.id'))
    register_date = Column(String(25))        # ngay dang ky

# Nhan vien co so chan nuoi
class dbFarmStaff(Base):
    __tablename__ = "farm_staff"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    farm_id = Column(Integer, ForeignKey('farms.id'))
    staff_name = Column(String(25))     # ten nhan vien

# Dieu kien chan nuoi
class dbCondition(Base):
    __tablename__ = "conditions"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    farm_id = Column(Integer, ForeignKey('farms.id'))
    condition = Column(String(255))      # dieu kien chan nuoi

# Giay chung nhan co so chan nuoi
class dbCertificate(Base):
    __tablename__ = "certificate"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    farm_id = Column(Integer, ForeignKey('farms.id'))
    certificate_num = Column(String(25))        # so giay chung nhan
    issue_date = Column(String(25))       # ngay cap

# Cơ sở chế biến sản phẩm chăn nuôi
class dbProcessing(Base):
    __tablename__ = "processing"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    farm_id = Column(Integer, ForeignKey('farms.id'))
    processing_name = Column(String(255))        # ten co so che bien
    processing_address = Column(String(255))     # dia chi co so
    processing_product = Column(String(255))      
    processing_date = Column(String(25))      # ngay cap giay phe

## Bang van ban phap luat
class dbLegal(Base):
    __tablename__ = "legal_documents"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255))      # tieu de van ban
    file = Column(String(255))       # duong dan file van ban
    issue_date = Column(String(25))       # ngay phat hanh