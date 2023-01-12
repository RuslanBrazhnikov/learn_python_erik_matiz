from random import randint
from random import choice

#
#
# my_list = ['wegf', 'sfgsfg', 'efgse', 'wefgwe']
#
# f = choice(my_list)
# print(f)
# print(randint(1, 9))

# class Die():
#     def __init__(self, sides):
#         self.sides = sides
#
#     def roll_die(self):
#         print(randint(1, self.sides))
#
#
# bros_1 = Die(20)
# bros_1.roll_die()
# bros_1.roll_die()
# bros_1.roll_die()
# bros_1.roll_die()
# bros_1.roll_die()
# bros_1.roll_die()
# bros_1.roll_die()
# bros_1.roll_die()
# bros_1.roll_die()
# bros_1.roll_die()
#
# my_list = [1, 322, 34, 6, 72, 4, 51, 734, 20, 8, 'd', 'e', 'w', 'q', 'l']
# p = choice(my_list)
# p_1 = choice(my_list)
# p_2 = choice(my_list)
# p_3 = choice(my_list)
# print(f'Билет содержащий комбинацию "{p}, {p_3}, {p_2}, {p_1}" является ВЫИГРЫШНЫМ!!!!')


# i = 0
# f = my_ticket[0]
# for i in my_ticket:
#     f = choice(my_ticket)
#     if i == 1 and i == 6 and i == 8 and i == 20:
#         print('Поздравляю!')
#     else:
#         i += 1


my_list = [1, 3, 8, 2, 8]
num = []

count = 0
while my_list != num:
    count += 1
    for i in range(5):
        num.append(randint(1, 8))
    if num != my_list:
        num = []
    else:
        print(num)
        print(f'Кол-во итераций {count}')