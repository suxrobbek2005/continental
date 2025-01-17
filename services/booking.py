from models.user import User
from models.room import Room
from models.book import Book

def booking(user: User, rooms: list[Room]) -> Book:
    room_number = int(input("room number: "))
    for room in rooms:
        if room.number == room_number:
            return Book(user, room)
        
def available_rooms(rooms: list[Room], bookings: list[Book]):
    return [room for room in rooms if not room in bookings]
