# my_list = ['sdf', 'ewf', 'efsef', 'fsefsef', 'sdf', 'sdf']
#
# new_list = []
#
# while my_list:
#     current = my_list.pop()
#     print(f'проверенныве пользователт {current}')
#     new_list.append(current)
#
# for i in new_list:
#     print(i.title())
#
# while 'sdf' in new_list:
#     new_list.remove('sdf')
# print(new_list)

# slovar = {}
#
# f = True
#
# while f:
#     name = input('Как тебя зовут: ')
#     golos = input('Да/нет: ')
#
#     slovar[name] = golos
#
#     zanovo = input('Следующтй голос? да/нет: ')
#     if zanovo == 'no':
#         f = False
#
# print('------ ОПРОС ЗАВЕРШЕН -----')
#
# for i, v in slovar.items():
#     print(f'{i} проголосовал - {v}')

# sandwich_orders = ['tomato', 'potato', 'pastrami', 'crash', 'pastrami', 'box']
#
# finished_sandwiches = []
#
# for i in sandwich_orders:
#     print(f'I made your tuna {i}')
#
# for i in sandwich_orders:
#     finished_sandwiches.append(i)
#     print(f'Sand is {i} GOTOV!')
#
# print('к сожалению пиццы pastrami больше нет(')
#
# while 'pastrami' in finished_sandwiches:
#     finished_sandwiches.remove('pastrami')
# print(finished_sandwiches)

dict = {}

f = True

while f:
    name = input('Как вас зовут?: ')
    place = input('Где бы вы хотели провести отпуск вашей мечты?: ')
    dict[name] = place
    next_people = input('Следующий гость? (да/нет): ')
    if next_people == 'нет':
        print('Выход ...')
        f = False

print('___ОПРОС ЗАВЕРШЕН___')
for i, v in dict.items():
    print(f'{i} хотел бы провести отпуск в {v}')