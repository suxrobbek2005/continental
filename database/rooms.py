class Room:
    rooms = [
        {"number": 101, "size": "single", "price": 50000},
        {"number": 102, "size": "double", "price": 75000},
        {"number": 103, "size": "suite", "price": 120000},
    ]

    @staticmethod
    def display_all_rooms():
        for room in Room.rooms:
            print(f"Xona: {room['number']}, O'lchami: {room['size']}, Narxi: {room['price']} so'm")
