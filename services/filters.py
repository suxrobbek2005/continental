from models.room import Room


def filter_rooms(rooms: list[Room], size: int, price: float) -> list[Room]:

    criteria = input("Filtrlash mezonini kiriting (size yoki price): ").lower()
    value = input("Qiymatni kiriting: ").lower()
    
    if criteria == "size":
        filtered = [room for room in Room.rooms if room["size"] == value]

    elif criteria == "price":
        filtered = [room for room in Room.rooms if room["price"] <= int(value)]

    else:
        print("Noto'g'ri mezon.")
        return

    for room in filtered:
        print(f"Xona: {room['number']}, O'lchami: {room['size']}, Narxi: {room['price']} so'm")

    return [room for room in rooms if room.size == size or room.price <= price]

from models.room import Room

    