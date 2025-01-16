from models.user import User
from models.room import Room
from models.book import Book
from services import authentications, booking, filters


def show_menu(menu: list[tuple[int, str]]):
    for option in menu:
        print(f"{option[0]} - {option[1]}")

def main():
    choice = 0

    user: User = None
    rooms: list[Room] = []
    users: list[User] = []
    session: list[User] = []
    bookings: list[Book] = []

    guest_menu = [
        (1, "Register"),
        (2, "Login"),
        (3, "Exit")
    ]

    user_menu = [
        (1, "See available rooms"),
        (2, "Book a room"),
        (3, "Filter rooms"),
        (4, "Logout"),
        (5, "Exit")
    ]

    while True:

        a_rooms = booking.available_rooms(rooms, bookings)

        while user:
            show_menu(user_menu)
            choice = input("choice: ")

            if choice == "1":
                for a_room in a_rooms:
                    print(f"Room number: {a_room.number}, Size: {a_room.size}, Price: {a_room.price}, Type: {a_room.type}")

            elif choice == "2":
                book = booking.booking(user, a_rooms)
                bookings.append(book)
                a_rooms.remove(book.room)

            elif choice == "3":
                size = int(input("size: "))
                price = float(input("price: "))

                filtered_rooms = filters.filter_rooms(a_rooms, size, price)
                for room in filtered_rooms:
                    print(f"Room number: {room.number}, Size: {room.size}, Price: {room.price}, Type: {room.type}")

            elif choice == "4":
                session = authentications.logout(user, session)
                user = None
            elif choice == "5":
                exit()
            else:
                print("invalid option")

        while user == None:
            show_menu(guest_menu)
            choice = input("choice: ")

            if choice == "1":
                user = authentications.register(users)
                users.append(user)
                session.append(user)

            elif choice == "2":
                user = authentications.login(users)
                if user:
                    session.append(user)

            elif choice == "3":
                exit()
            else:
                print("invalid option")

if __name__ == "__main__":
    main()