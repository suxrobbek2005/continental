from models.room import Room


def filter_rooms(rooms: list[Room], size: int, price: float) -> list[Room]:
    return [room for room in rooms if room.size == size or room.price <= price]