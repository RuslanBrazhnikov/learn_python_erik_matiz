# filename = 'programming.txt'
#
# with open(filename, 'w') as file_project:
#     file_project.write('I love Python\n')
#     file_project.write('I love Python\n')
#
# with open(filename, 'a') as file_project:
#     file_project.write('osdhigviwhgihwighoqweg\n')
#     file_project.write('osdhigviwhgihwighoewrgdsrgjiwerhg83 497t89347t94738375897435984qweg\n')


# file = 'guest.txt'
#
# with open(file, 'w') as file_project:
#     name = input('Введите ваше имя: ')
#     file_project.write(name)

# file = 'guest_book.txt'
#
# with open(file, 'w') as file_project:
#     f = True
#     while f:
#         name = input('Введие ваще имя: ')
#         print(f'Приветствуем вас {name}')
#         file_project.write(f'Приветствуем вас {name}\n')
#         print('Ваше имя сохранилось в файле!')
#         reapet = input('Введите команду "нет" для выхода из программы или любую для продолжения...')
#         if reapet == 'нет':
#             print('Выход...')
#             f = False

file = 'ask.txt'

with open(file, 'w') as p:
    f = True
    while f:
        ask_question = input('Ответьте на вопрос почему вам нравится програмирование?: ')
        print('Спасибо ваш ответ сохранился в файле!')
        p.write(f'{ask_question}\n')
        repeat = input('введите комамнду  выход для выхода из программы или любую для пролжения...')
        if repeat == 'выход':
            print('выход...')
            f = False