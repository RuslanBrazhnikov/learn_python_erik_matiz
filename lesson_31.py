# filename = 'pi_digits.txt'
#
# with open(filename) as file_object:
#     lines = file_object.readlines()
#
# pi_string = ''
# for line in lines:
#     pi_string += line.rstrip()
#
# print(pi_string)
# print(len(pi_string))

# filename = 'pi_million_digits.txt'
#
# with open(filename) as file_object:
#     lines = file_object.readlines()
# pi_string = ''
# for line in lines:
#     pi_string += line.rstrip()
#
# birdhday = input('Введите ваш день рождения: ')
# if birdhday in pi_string:
#     print('Ваша дата рождения входит в милион!')
# else:
#     print('Дата не входит ')

filename = 'learning_python.txt'

with open(filename) as file_project:
    lines = file_project.readlines()
    for line in lines:
        print(line.replace('g', '9845634657489326547836507134650234650782345678').rstrip())








