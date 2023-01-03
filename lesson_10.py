sq = []

for i in range(1, 11):
    sq.append(i**2)
print(sq)

digits = [1, 2, 5, 657, 34, 6, 23, 7, 3, 9, 245, 2345, 34]
print(min(digits))

digits = [i**2 for i in range(1, 11)]
print(digits)

my_list = []

for i in range(1, 1000001):
    my_list.append(i)
print(my_list)
print(min(my_list))
print(max(my_list))
print(sum(my_list))

for i in range(3, 30):
    if i % 3 == 0:
        my_list.append(i)

print(my_list)

for i in range(1, 10):
    my_list.append(i**3)
print(my_list)

my_list = [i**3 for i in range(1, 10)]
print(my_list)