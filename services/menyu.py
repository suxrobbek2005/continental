from colorama import Fore, Style
from models.room import Room
from models.user import User
from models.book import Book
from pprint import pprint

def menu():
    print("""
Buyruqlar ketmaketligi: 
Ruyxatdan o`tish: 1
Dasturga kirish:  2
Chiqish: 3
        """)
    
def book_user(rooms: Room, user_book: User):
    
   
    while True:
        print("""
Buyruqlar ketmaketligi: 
Xonalar haqida ma`lumotni olish: 1
Xonani band qilish:  2
Orqaga: 3
Dasturdan chiqish: 4
        """)

        number = input(f"{Style.DIM},{Fore.GREEN},Buyruqni kiriting --> {Style.RESET_ALL} ")

        if number == '1':

            print(f"{Style.DIM},{Fore.LIGHTBLUE_EX} == Xonalar ruyxati == {Style.RESET_ALL}")

            for xona in rooms:

                print(f"Xona nommiri: {xona['number']}\nXonalar soni: {xona['size']}\nXona narxi: {xona['price']}\nXona turi: {xona['type']}\n")
        
        elif number == '2':

            while True:

                number_room = input(f"{Style.DIM},{Fore.LIGHTCYAN_EX}Band qilmoqchi bo`lgan xona nomirini kiriting --> {Style.RESET_ALL} ")

                for xona in rooms:

                    if str(number_room) == str(xona["number"]):

                        print(f"{Style.DIM},{Fore.LIGHTGREEN_EX}Sizning tanlovingiz juda ajoyib bo`ldi\n {Style.RESET_ALL}")

                        return Book(user_book, xona)
                    
                print(f"{Style.DIM},{Fore.LIGHTMAGENTA_EX}Siz kiritkan nommir bron qilingan, iltimos boshqa nomirni tanlang!\n {Style.RESET_ALL}")

        elif number == '3':

            break

        elif number == '4':

            print(f"{Style.DIM},{Fore.LIGHTMAGENTA_EX}Bizning hizmatimizdan foydalanganingizdan hursandmiz {Style.RESET_ALL}")
            exit() 

        else:        
            print(f"{Style.DIM},{Fore.LIGHTMAGENTA_EX}Siz noto`g`ri buyrug kiritdingiz {Style.DIM},{Fore.LIGHTMAGENTA_EX}")