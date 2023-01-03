# my_list = ['admin', 'chill', 'john', 'deil', 'stive']
#
# for i in my_list:
#     if i == 'admin':
#         print(f'\tПриветствуем вас {i}! не хотите ли узнать статус сайта?')
#     else:
#         print(f'Приветствуем вас на нашем сайте {i}!')
#
# for i in range(0, len(my_list)):
#     my_list.pop()
# print(my_list)
#
# if my_list == []:
#     print('Нам нужны посетители!!!')

# current_users = ['admin', 'chill', 'john', 'deil', 'stive']
#
# new_users = ['Admin', 'bred', 'john', 'curell', 'lina']
#
#
#
#
# for i in new_users:
#     if i.lower() in current_users:
#         print('Выберите другое имя')
#     else:
#         print('Okay')

list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in list_numbers:
    print(i)

for i in list_numbers:
    if i == 1:
        print(f'{i}st')
    elif i == 2:
        print(f'{i}nd')
    elif i == 3:
        print(f'{i}rd')
    else:
        print(f'{i}th')