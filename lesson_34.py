import json


#
# numbers = [2, 3, 4, 2, 4, 22, 33, 2]
#
# file = 'numbers.json'
# with open(file, 'w') as f:
#     json.dump(numbers, f)

# file_1 = 'numbers.json'
#
# with open(file_1) as f:
#     numbers = json.load(f)
#
# print(numbers)

def get_stored_username():
    file = 'username.json'

    try:
        with open(file) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input('Введите ваше имя: ')
    file = 'username.json'
    with open(file, 'w') as f:
        json.dump(username, f)
    return username
def greet_user():
    """Приветствует пользователя по имени."""
    file = 'username.json'
    username = get_stored_username()
    print(f'Ваше имя {username}')
    name = input('Правильно ли определено имя пользователя?: ')
    if name == 'нет':
        username = get_new_username()
        print('Отлично сохранили!')
    else:
        print(f'С возврашением! {username}')


greet_user()

# def new_num():
#         num = int(input('Введите число: '))
#         file = 'number.json'
#         with open(file, 'w') as f:
#             json.dump(num, f)
#         return num
# def get_num():
#     file = 'number.json'
#     try:
#         with open(file) as f:
#             num = json.load(f)
#     except FileNotFoundError:
#         return None
#     else:
#         return num
# def know_num():
#     num = get_num()
#     if num:
#         print(f'Привет! Я помню ваше число! это - {num}!')
#     else:
#         num = new_num()
#         print(f'Спасибо! Постараюсь запомнить :) число - {num}!')
#
# know_num()

