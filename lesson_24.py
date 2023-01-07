my_list = ['sedkh', 'easdfifveo', 'uieasgfucg', 'aeifg', 'ifhihf']

def show_messages(list):
    for i in list:
        print(i)

show_messages(my_list)

print('')

sent_messages = []
def send_messages(list, list_2):
    while list:
        current = list.pop()
        list_2.append(current)
        print(list_2)

print('')
send_messages(my_list[:], sent_messages)




print('-----------------------')
print(my_list)
print('-----------------------')
print(sent_messages)



