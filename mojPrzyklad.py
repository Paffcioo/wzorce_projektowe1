# name1 = input('Podaj swoje imię:')
name_multi = ['dsd', 'Dfg', 'Cgj', 'ike', 'lko', 'Gvw']
# name_multi.append(input('Podaj jakieś imię:'))
name2 = ['Ksd', 'lko', 'Dfa']


def adderMultiplier(func):
    def inner(list, new_name):
        if type(new_name) == str:
            list.append(new_name)
        else:
            for name in new_name:
                list.append(name)
    return inner


@adderMultiplier
def nameAdder(list, new_name):
    list.append(new_name)


# @nameMultiplier
def bigOnesOnly(func):
    def checker(name):
        if name[0].isupper():
            print(f'Hej, {name}!!!', end=', ')
            # return
        # return func(name)
    return checker


@bigOnesOnly
def namePrinter(name):
    print(f'Hej, {name}')
    # else:
    #     pass


def nameMultiplier(list):
    # def inner(list):
        for name in list:
            namePrinter(name)
            # print(f'Czołem, {name}!')
    # return inner


# nameAdder(name_multi, input('Podaj jakieś imię:'))
# nameAdder(name_multi, 'name2')
# nameAdder(name_multi, 'Name3')

# nameAdder(name_multi, name2)
# nameMultiplier(name_multi)
# print('Ostateczna lista wsadowa:', name_multi)