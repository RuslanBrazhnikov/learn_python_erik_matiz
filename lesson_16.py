# alien_0 = {'color': 'green', 'points': 5}
#
# print(alien_0['color'])
# print(alien_0['points'])
#
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
#
# print(alien_0)
#
# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
#
# print(f"original position: {alien_0['x_position']}")
#
# if alien_0['speed'] == 'slow':
#     x_inc = 1
# elif alien_0['speed'] == 'medium':
#     x_inc = 2
# else:
#     x_inc = 3
#
# alien_0['x_position'] = alien_0['x_position'] + x_inc
#
# print(f"New position: {alien_0['x_position']}")


# people_info = {
#     'first_name': 'Ruslan',
#     'last_name': 'Brazhnikov',
#     'age': 27,
#     'city': 'Sterlitamak',
# }
#
# print(people_info)

# dict_number = {
#     'my': 5,
#     'sister': 9,
#     'momy': 7,
#     'bro': 3,
# }
#
# print(f"Любимое число сестры {dict_number['sister']}, а брата {dict_number['bro']}")

# dict_python = {
#     'переменные':
#         ' - это временные ячейки памяти в которых хранятся какие либо данные',
#
#     'if':
#         ' - Это ветка условие',
# }
#
# for i, v in dict_python.items():
#     print(i,v)

# dict_rivers = {
#     'egipt': 'nil',
#     'russia': 'volga',
#     'sterlik': 'seleuk',
# }
#
# for i, v in dict_rivers.items():
#     print(f"В стране {i} течет река {v}")
#
# for i in dict_rivers.values():
#     print(i)
# for i in dict_rivers.keys():
#     print(i)


dict_people = {
    'me': 'c',
    'he': 'c#',
    'she': 'python',
    'opros': 'c++',
}



for i in dict_people.keys():
    if i == 'opros':
        print(f"Спасибо вам {i} за участие")
    else:
        print(f"{i} Пройдите пожалуйста опрос!")
