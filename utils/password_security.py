import bcrypt

def hash_password(password) -> str:
    password_to_bytes = password.encode()
    #Blowfish cipher
    salt = bcrypt.gensalt()
    hashed_salted_password = bcrypt.hashpw(password_to_bytes, salt)
    return hashed_salted_password

def verify_password(hashed_salted_password, password) -> bool:
    password_to_bytes = password.encode()
    password_check = bcrypt.checkpw(password_to_bytes, hashed_salted_password)
    return password_check