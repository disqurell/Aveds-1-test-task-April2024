from hashlib import sha512


def hash_password(password: str):
    hashed = sha512(password.encode())
    return str(hashed.hexdigest())


def validate_password(password_in_db: str, password_to_check: str):
    return hash_password(password_to_check) == password_in_db
