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