def func_sand(*sand):
    print(f'{sand} - Это отличный выбор!')


# func_sand('egg', 'milk', 'potato')
# func_sand('egg', 'milk')
# func_sand('egg')


def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


# user = build_profile('Ruslan', 'Dennis', location='STR', field='Chesyet')
#
# print(user)


def func_cars(zavod, name_model, **kwargs):
    kwargs['Производитель'] = zavod
    kwargs['Название модели'] = name_model
    return kwargs


# car = func_cars('УАЗ', 'Патриот', color='белый', motor='1.6')
#
# print(car)
