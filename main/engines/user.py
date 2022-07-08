import bcrypt

from main.models.user import User

# No schemas in engines


def get_user_info(_id: int) -> User:
    user = User.find_by_id(_id)
    return user


def check_user_exist(email: str) -> bool:
    if User.find_by_email(email) is None:
        return False
    else:
        return True


def create_user(name: str, email: str, password: str) -> User:
    if check_user_exist(email):
        raise ValueError("User already exists")
    else:
        hashed_password = hash_password(password)
        new_user = User(name=name, email=email, hashed_password=hashed_password)
        new_user.save_to_db()
        return new_user


def hash_password(password: str) -> str:
    password = bytes(password, "utf-8")
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    hashed = hashed.decode("utf-8")
    return hashed


def check_hashed_password(password: str, hashed_password: str) -> bool:
    password = bytes(password, "utf-8")
    hashed_password = bytes(hashed_password, "utf-8")
    return bcrypt.checkpw(password, hashed_password)


def verify_user(email: str, password: str) -> bool:
    user = User.find_by_email(email)
    if user is None:
        raise LookupError("User does not exist")
    else:
        hashed = user.hashed_password
        return check_hashed_password(password, hashed)
