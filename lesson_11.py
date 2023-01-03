# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# friends = players[:]
# print(friends)



# print('The irst three items in the list are: ')
# print(*players[:3])
#
# print('The irst three items in the list are: ')
# print(*players[1:4])
#
# print('The last three items in the list are:')
# print(*players[2:])

my_pizza = ['peperoni', 'mozzarela', 'salami']

friend_pizza = my_pizza[:]

print(my_pizza)
print(friend_pizza)

my_pizza.append('Cheeze')
friend_pizza.append('Meeat')

print('My favorite pizzas are:')

for i in my_pizza:
    print(i)

print('My friend’s favorite pizzas are:')

for i in friend_pizza:
    print(i)