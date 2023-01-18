# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")
# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("Second number: ")
#     if second_number == 'q':
#         break
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print('Деление на 0 неыозможго')
#     else:
#         print(answer)

# filename = 'alice.txt'
#
# try:
#     with open(filename, encoding='utf-8') as f:
#         contents = f.read()
# except FileNotFoundError:
#     print('Файла нет')
# else:
#     print('Отлично файд создан')
#     n = contents.split()
#     w = len(n)
#     print(w)


# def count_words(file):
#     """Подсчет приблизительного количества слов в файле."""
#     try:
#         with open(file, encoding='UTF-8') as f:
#             contents = f.read()
#     except FileNotFoundError:
#         pass
#     else:
#         words = contents.split()
#         num_words = len(words)
#         num_letters = len(contents)
#         print(f'В файле {file} имеется {num_words} слов, а символов {num_letters}')
#
# filenames = ['alice.txt', 'siddhi.txt', 'moby_dick.txt']
# for filename in filenames:
#     count_words(filename)
#
# f = True
# while f:
#     try:
#         name = int(input('Введите число: '))
#         name1 = int(input('Введите второе чило: '))
#         sum_words = name1 + name
#     except ValueError:
#         print('Введите пожалуйста число а не тест!!!')
#     else:
#         print(sum_words)
#         f = False

# file = 'cats.txt'
# file1 = 'dogs.txt'
#
# try:
#     with open(file, encoding='UTF-8') as f:
#         f = f.read()
#         print(f)
# except FileNotFoundError:
#     pass
#
# try:
#     with open(file1, encoding='UTF-8') as f:
#         f = f.read()
#         print(f)
# except FileNotFoundError:
#     pass


file = 'text.txt'

with open(file, encoding='UTF-8') as f:
    m = f.read()
    print(m.lower().count('the '))
