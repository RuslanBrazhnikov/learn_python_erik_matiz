# def get_name(name, sourname, middle=''):
#     full_name = f'{name} {sourname}'
#     return full_name.title()
#
#
# rus = get_name('ruslan', 'brazhnikov')
# print(rus)
#
#
# def build_person(first_name, last_name):
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person
# musician = build_person('jimi', 'hendrix', age=27)
#
#
#
# print(musician)


# def city_country(name_city, name_country, road='None'):
#     return f'{name_city}, {name_country}'
#
# print(city_country('ufa', 'rb'))
# print(city_country('moscow', 'russia'))
# print(city_country('rostov', 'russia'))


def make_album(name_son, name_album, road=None):
    name = {name_son: name_album}
    if road:
        name['road'] = road
    return name

dcis = make_album('oxxx', 'm,ox')
print(dcis)

while True:
    name = input('Введиет название альбома: ')
    isp = input('Введите исполнителя: ')
    print(make_album(name, isp))
    reapet = input('Хотите выбрать еще раз? (да\нет): ')
    if reapet == 'нет':
        print('ВЫХОД ИЗ ПРОГРАММЫ........')
        break