"""Класс для представления автомобиля."""


class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometr_reading = 0

    def get_descriptive_name(self):
        long_name = f'{self.year} {self.model} {self.make}'
        return long_name.title()

    def read_odometr(self):
        print(f'This car has {self.odometr_reading} miles on it.')

    def update_odometr(self, mily):
        if mily >= self.odometr_reading:
            self.odometr_reading = mily
        else:
            print('Ты не можешь сбрасывать показания одометра')

    def increment_odometr(self, miles):
        self.odometr_reading += miles


# class Battery():
#     """Простая модель аккумулятора электромобиля."""
#
#     def __init__(self, battery_size=70):
#         self.battery_size = battery_size
#
#     def describe_battery(self):
#         print(f"This car has a {self.battery_size}-kWh battery.")
#
#     def get_range(self):
#
#         """Выводит приблизительный запас хода для аккумулятора."""
#
#         if self.battery_size == 75:
#             range = 260
#         elif self.battery_size == 100:
#             range = 315
#         print(f"This car can go about {range} miles on a full charge.")


class Electrik(Car):
    def __init__(self, model, make, year):
        super().__init__(make, model, year)
        self.battery = Batery()


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
