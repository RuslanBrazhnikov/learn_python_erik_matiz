# aliens = []
# # Создание 30 зеленых пришельцев.
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)
# # Вывод первых 5 пришельцев:
# for alien in aliens[:5]:
#     print(alien)
# print("...")
# # Вывод количества созданных пришельцев.
# print(f"Total number of aliens: {len(aliens)}")
#
# for alien in aliens[0:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = 10
#
# for alien in aliens[0:5]:
#     print(alien)
# print('...')


# favorite_languages = {
#     'jen': ['python', 'ruby'],
#     'sarah': ['c'],
#     'edward': ['ruby', 'go'],
#     'phil': ['python', 'haskell'],
# }
# for name, languages in favorite_languages.items():
#     if len(languages) > 1:
#         print(f'\n{name.title()}s favorite languages are:')
#     else:
#         print(f"\n{name.title()}'s favorite languages is:")
#     for language in languages:
#         print(f"\t{language.title()}")


# users = {
#     'aeinstein': {
#         'first': 'albert',
#         'last': 'einstein',
#         'location': 'princeton',
#     },
#     'mcurie': {
#         'first': 'marie',
#         'last': 'curie',
#         'location': 'paris',
#     },
# }
# for username, user_info in users.items():
#     print(f"\nUsername: {username}")
#     full_name = f"{user_info['first']} {user_info['last']}"
#     location = user_info['location']
#     print(f"\tFull name: {full_name.title()}")
#     print(f"\tLocation: {location.title()}")

# people = []
#
# dict_me = {
#     'age': 27,
#     'pol': 'muzh',
#     'rost': 183,
# }
#
# dict_bro = {
#     'age': 22,
#     'pol': 'muzh',
#     'rost': 190,
# }
#
#
# for i in range(1):
#     me = {'age': 27, 'pol': 'muzh', 'rost': 183}
#     people.append(me)
#     bro = {'age': 22, 'pol': 'muzh', 'rost': 190}
#     people.append(bro)
#
# for i in people:
#     print(i)
#
# for i, v in me.items():
#     print(f"Me\n{i}: {v}")
#     for r, t in bro.items():
#         print(f"Bro\n{r}: {t}")


favorite_places = {
    'me': ['str', 'ufa', 'salsvat'],
    'bro': ['piter', 'rostov', 'penza']
}

for i, v in favorite_places.items():
    print(f'{i}: {v}')