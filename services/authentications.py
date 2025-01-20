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


def register(users: list[User]) -> User:
    name = input("Ismni kiriting: ")
    while not name.isalpha():
        print("xato name kiritdingiz!\n")
        name = input("Ismni kiriting: ")

    age = input("Yoshingizni kiriting: ")
    while not age.isdigit() or int(age) < 18:
        print("xato ma`lumot kiritdingiz!\n")
        age = input("Yoshingizni kiriting: ")

    username = input("username ni kiriting: ")
    while is_user(users, username):
        print("Bunday foydalanuvchi ruyxatdan o`tgan!\n")
        username = input("username ni kiriting: ")

    password = input("password ni kiriting: ")
    while not check_password(password):
        print("Kuchsiz parol kiritdingiz, iltimos qaytadan kiriting!\n")
        password = input("password ni kiriting: ")

    print("Siz muvaffaqiyatli ruyxatdan o`tdingiz! \n")
    return User(name, age, username, password)
# Login function orqali bar
def login(users: list[User]) -> User:
    # bazada bor bo`lgan userni topmaguncha aylanadi
    while True:
        username = input("username ni kiriting: ")
        password = input("password ni kiriting: ")


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