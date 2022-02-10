class Lemonade:

    def __init__(self, flavor="Обычная газировка"):
        self.__flavor = flavor

    @property
    def flavor(self):
        return self.__flavor

    @flavor.setter
    def flavor(self, flavor):
        if isinstance(flavor, str):
            self.__flavor = flavor
        else:
            self.__flavor = None

    def drink_info(self):
        if self.flavor:
            print(f'Газировка и {self.__flavor}')
        else:
            print(f'Обычная газировка')


f1 = Lemonade('клубника')
f1.drink_info()


# class House:
#     def __init__(self, room_count, consist):
#         self.room_count = room_count
#         self.consist = consist
#     @property
#     def show_info(self):
#         return f'кол-во коинат: {self.room_count}\nсостав:{self.consist}'
#
#
#
# h1 = House(room_count=6, consist='кирпич')
# print(h1.show_info)

