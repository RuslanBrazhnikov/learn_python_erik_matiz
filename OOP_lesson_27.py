class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f'{self.name} is now sitting')

    def roll_over(self):
        print(f'{self.name} rolled over!')


my_dog = Dog('Dikson', 7)
your_dog = Dog('Lina', 9)

print(f'My dogs name is {my_dog.name}.')
print(f'My dog is {my_dog.age} years old.')
my_dog.sit()
my_dog.roll_over()

print(f'My dogs name is {your_dog.name}.')
print(f'My dog is {your_dog.age} years old.')
your_dog.sit()
your_dog.roll_over()

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cisine_type = cuisine_type
        self.

    def describe_restaurant(self):
        print(f'{self.restaurant_name} {self.cisine_type}')

    def open_restaurant(self):
        print(f'The {self.restaurant_name} is OPEN!')

restaurant = Restaurant('HAN', 'SWEET')

print(f'Restoran {restaurant.restaurant_name} {restaurant.cisine_type}')
restaurant.open_restaurant()
restaurant.describe_restaurant()


restaurant_shaitan = Restaurant('Shaitan', 'Meat')
restaurant_shaitan_1 = Restaurant('Fox and Dogs', 'Sugar')
restaurant_shaitan_2 = Restaurant('Bazar', 'Shaurma')

restaurant_shaitan.describe_restaurant()
restaurant_shaitan_1.describe_restaurant()
restaurant_shaitan_2.describe_restaurant()


class User():
    def __init__(self, first_name, last_name, age, adress):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.adress = adress

    def describe_user(self):
        print(f'{self.first_name} {self.last_name} and his {self.age} years old, and adress is {self.adress}')

    def greet_user(self):
        print(f'Helloo {self.first_name} {self.last_name}!!!')

user_1 = User('Ruslan', 'Brazhnikov', 27, 'STR')
user_2 = User('Denis', 'Brazhnikov', 22, 'BALI')

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

