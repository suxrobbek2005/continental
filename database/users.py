users = []


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @staticmethod
    def add_user(username, password):
        users.append(User(username, password))

    @staticmethod
    def authenticate(username, password):
        return any(user.username == username and user.password == password for user in users)
