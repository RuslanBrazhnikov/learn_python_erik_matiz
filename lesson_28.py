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


my_new_car = Car(2019, 'A4', 'Audi')
print(my_new_car.get_descriptive_name())
my_new_car.update_odometr(2)
my_new_car.read_odometr()
my_new_car.increment_odometr(23)
my_new_car.read_odometr()

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cisine_type = cuisine_type
        self.number_serving = 0

    def describe_restaurant(self):
        print(f'{self.restaurant_name} {self.cisine_type}')

    def open_restaurant(self):
        print(f'The {self.restaurant_name} is OPEN!')
    def set_number_served(self, count):
        self.number_serving += count
        print(f'Количество обслуженных гостей = {count}')

restaurant = Restaurant('HAN', 'SWEET')
restaurant.set_number_served(3)

print(f'Restoran {restaurant.restaurant_name} {restaurant.cisine_type}')
restaurant.open_restaurant()
restaurant.describe_restaurant()

class User():
    def __init__(self, first_name, last_name, age, adress):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.adress = adress
        self.login_attempts = 0

    def describe_user(self):
        print(f'{self.first_name} {self.last_name} and his {self.age} years old, and adress is {self.adress} {self.login_attempts}')

    def greet_user(self):
        print(f'Helloo {self.first_name} {self.last_name}!!!')
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0

user = User('Ruslan', 'Brazhnikov', 27, 'STR')

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

user.reset_login_attempts()

user.describe_user()

