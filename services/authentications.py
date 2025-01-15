from models.user import User

def is_user(users: list[User], username: str) -> bool:
    for user in users:
        if user.username == username:
            return True
    
    return False

def check_password(password: str) -> bool:
    u, l, d, p = False, False, False, False

    for char in password:
        if char.isupper():
            u = True
        elif char.islower():
            l = True
        elif char.isdigit():
            d = True
        elif char in "!@#$%^&*()":
            p = True

    return all([u, l, d, p])


def register() -> User:
    name = input("name: ")
    while not name.isalpha():
        print("invalid name")
        name = input("name: ")

    age = input("age: ")
    while not age.isdigit() or int(age) < 18:
        print("invalid age")
        age = input("age: ")

    username = input("username: ")
    while is_user(username):
        print("invalid username")
        username = input("username: ")

    password = input("password: ")
    while not check_password(password):
        print("invalid password")
        password = input("password: ")

    return User(name, age, username, password)

def login(users: list[User]) -> User:
    username = input("username: ")
    password = input("password: ")

    if is_user(users, username) and check_password(password):
        for user in users:
            if user.username == username and user.password == password:
                return user
        
    return None

def logout(user: User, session: list[User]) -> bool:
    if user in session:
        session.remove(user)
        return True
    
    return False
