from lesson_28 import Car


#
# my_tesla = Electrik('tesla', 'model s', 2019)
# print(my_tesla.get_descriptive_name())
# my_tesla.batareya.describe_batery()
# my_tesla.batareya.get_range()


# class Restaurant():
#     def __init__(self, restaurant_name, cuisine_type):
#         self.cuisine_type = cuisine_type
#         self.restaurant_name = restaurant_name
#         self.cisine_type = cuisine_type
#
#     def describe_restaurant(self):
#         print(f'{self.restaurant_name} {self.cuisine_type}')
#
#     def open_restaurant(self):
#         print(f'The {self.restaurant_name} is OPEN!')
#
#
# class IceCreamStand(Restaurant):
#     def __init__(self, restaurant_name, cuisine_type):
#         super().__init__(self, restaurant_name)
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.flavors = 0
#
#     def print_ice(self):
#         dict = {}
#         f = True
#         while f:
#             self.flavors = 0
#             dic = input('Введите значения: ')
#             dic_1 = input('Введи второе значение: ')
#             dict[dic] = dic_1
#
#             rep = input('Еще раз?')
#
#             if rep == 'нет':
#                 print('выход')
#
#                 f = False
#                 self.flavors += 1
#
#         return print(f'{dict} -- {self.flavors}')
#
#
# ice = IceCreamStand('PAB', 'SWEET')
# ice.print_ice()

class User:
    def __init__(self, first_name, last_name, privileges):
        self.first_name = first_name
        self.last_name = last_name
        self.privileges = privileges

    def describe_user(self):
        print(
            f'{self.first_name} {self.last_name}')

    def greet_user(self):
        print(f'Helloo {self.first_name} {self.last_name}!!!')


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(self, first_name, last_name)
        self.first_name = first_name
        self.last_name = last_name

    def show_privileges(self):
        print(f'Можете выбрать привилегию --- {self.privileges}')


us = Admin('Ruslan', 'Brahnikov')
us.show_privileges()


class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges
        self.admin = Admin('f', 'sf')

    def show_privileges(self):
        print(f'Можете выбрать привилегию --- {self.privileges}')


pop = Privileges('sdefg')
po = Admin('wef', 'esf')
po.show_privileges()


class Batery():
    def __init__(self, batery_size=100):
        self.batery_size = batery_size

    def describe_batery(self):
        print(f'This car has a {self.batery_size}--kWh batery')

    def get_range(self):
        if self.batery_size == 75:
            ran = 260
        elif self.batery_size == 100:
            ran = 315
        print(f'This car go about {ran} and batary = {self.batery_size}mAh miles on a full charge')

    def upgrade_battery(self, bat):
        if bat != 100:

            print(f'Batary size {bat}')


class Electrik(Car):
    def __init__(self, model, make, year):
        super().__init__(make, model, year)
        self.batareya = Batery()


my_100 = Electrik('bmw', 'xxxx', 2022)
my_100.batareya.get_range()
my_100.batareya.upgrade_battery(75)
my_100.batareya.get_range()
my_100.batareya.upgrade_battery(100)
my_100.batareya.get_range()
