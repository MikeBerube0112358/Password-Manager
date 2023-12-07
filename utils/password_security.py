import bcrypt

def hash_password(password) -> str:
    password_to_bytes = password.encode()
    hashed_salted_password = bcrypt.hashpw(password_to_bytes, bcrypt.gensalt())
    return hashed_salted_password

def verify_password(hashed_salted_password, password) -> bool:
    password_to_bytes = password.encode()
    password_check = bcrypt.checkpw(hashed_salted_password, password_to_bytes)
    return password_check