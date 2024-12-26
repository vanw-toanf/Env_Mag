import bcrypt

class Hash:
    """
    Ma hoa mat khau nguoi dung
    Kiem tra mat khau duoc cung cap co trung voi mat khau da ma hoa hay khong
    """
    # Hash a password
    def bcrypt(password):
        """
        Ma hoa mat khau
        Chuyen doi dang str sang byte de xu ly
        :param password:
        :return:
        """
        pwd_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password=pwd_bytes, salt=salt)
        return hashed_password.decode('utf-8')

    # Check if the provided password matches the stored password (hashed)
    def verify(plain_password, hashed_password):
        """
        Kiem tra mat khau co trung mat khau da ma hoa khong
        Chuyen doi dang str sang byte de xu ly
        :param plain_password:
        :param hashed_password:
        :return:
        """
        password_byte_enc = plain_password.encode('utf-8')
        hashed_password_byte = hashed_password.encode('utf8')
        return bcrypt.checkpw(password=password_byte_enc, hashed_password=hashed_password_byte)
