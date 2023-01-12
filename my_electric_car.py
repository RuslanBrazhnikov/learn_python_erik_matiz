from car import Electrik

my_tesla = Electrik('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_batery()
my_tesla.battery.get_range()
