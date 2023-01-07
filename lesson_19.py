# num = 1
#
# while num <= 19:
#     print(num)
#     num += 1


# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     print(message)

# word = 'Введите слово, либо для завершения прогрмаммы введите q: '
#
# mes = ''
# while mes != 'q':
#     mes = input(word)
#     print(mes)
#     if mes == 'q':
#         print('Выход...')

# active = True
# while active:
#     mes = input(word)
#     if mes == 'q':
#         active = False
#     else:
#         print(mes)

# num = 0
#
# while num < 10:
#     num += 1
#     if num % 2 != 0:
#         continue
#
#     print(num)

# pizza = 'Введите желаемый топпинг: '
#
# f = True
# mes = ''
# while f:
#     mes = input(pizza)
#     print(f'{mes} vkluchen')
#     if mes == 'q':
#         print('esit')
#         f = False


age = int(input('Введите пожалуйста ваш возраст, либо для выхода из программы наберите -1: '))

mes = 'Введите пожалуйста ваш возраст, либо для выхода из программы наберите -1: '

while True:
    if age <= 3 and age != -1:
        print('Цена на билет 0')
        age = int(input(mes))
    elif age > 3 or age == 12:
        print('Цена на билет 10$')
        age = int(input(mes))
    elif age > 12:
        print('Цена на билет 15$')
        age = int(input(mes))
    else:
        if age == -1:
            print('Выход')
            break
