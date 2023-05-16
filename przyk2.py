def check_name(func):
    def inner(name):
        if name[0].isupper():
            print(f"Hej {name}")
            return
        return func(name)

    return inner


@check_name
def user_name(name):
    print("Witam")


user_name("Michał")

# przykład 2

def prettier(func):
    def check_name(a):
        if a[0].islower():
            print(f"Hej {a} z dużej litery!")
            return
        return func(a)
    return check_name
@prettier
def give_name(a):
    print(f"Hej {a}")
give_name("Ola")