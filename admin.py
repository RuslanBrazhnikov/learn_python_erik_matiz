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

class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges
        self.admin = Admin('f', 'sf')

    def show_privileges(self):
        print(f'Можете выбрать привилегию --- {self.privileges}')