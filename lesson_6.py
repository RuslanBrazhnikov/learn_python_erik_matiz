names = ['Ancle', 'Dady', 'Brother']

for i in range(0, len(names)):
    print(f'Уважаемый {names[i]}, приглашаем вас на вечерний ужин!')

print(f'\tДорогие гости, {names[1]}, к большому сожалению прийти не сможет')

del names[1]

names.append('Mommy')
print(f'Вместо него придет {names[-1]}')

for i in range(0, len(names)):
    print(f'Уважаемый {names[i]}, приглашаем вас на вечерний ужин!')
print()

print('Дорогие гости, мы купили новый стол и можем пригласить еще 3 гостей')

names.insert(0, 'Sister')
print(names)

names.insert(2, 'John')
print(names)

names.append('Lucas')
print(names)

print()

for i in range(0, len(names)):
    print(f'Уважаемый {names[i]}, приглашаем вас на вечерний ужин!')

print('Дорогие наши гости, только что мы узнали что новый стол не успеют привезти вовремя и места хватит только для двх гостей(')

print()

print(*names, sep=', ')

new_names = []

for i in range(0, 2):
    new_names.append(names.pop(i))

print(*new_names, sep=', ', end='.')
print()

for i in range(len(new_names)):
    print(f'Дорогой {new_names[i]} ранее озвученное приглашение остается в силе!')


for i in range(len(new_names)):
    del new_names[i]


print(new_names)


