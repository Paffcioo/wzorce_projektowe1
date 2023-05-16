from abc import ABC, abstractmethod


def make_pretty(func):
    def inner():
        print('I got decorated')
        func()

    return inner


@make_pretty
def ordinary():
    print('I am ordinary')

    # ordinary()

    # decoration = make_pretty(ordinary)
    # decoration()

    # def smart_divide(func):
    def inner1(a, b):
        print(f'I am going to divide {a} and {b}, but let me check it out!')
        if b == 0:
            print('Cannot divide')
            return
        return func(a, b)

    return inner1()


# @smart_divide
def divide(a, b):
    return a / b


# print(divide(2, 5))
# print(divide(3, 0))


def decorate_cake(func):
    def some_cake():
        func()
        ingredients = ['pineapple', 'blueberries', 'crumble']
        for i in ingredients:
            print(f'Giving {i} on my sponge cake')

    return some_cake


@decorate_cake
def sponge_cake():
    print("I am a simple sponge cake!")


# sponge_cake()

'''
Zad1. Uczenie kultury użytkownika - jeśli ktoś przekaże do funkcji imię z małej to nie wyświetla się powitanie, \n 
a jeśli wielką to napisz " Hej {imie}!"
'''

# name1 = input('Podaj swoje imię:')
name_multi = ['dsd', 'Dfg', 'Cgj', 'ike', 'lko', 'Gvw']
name2 = ['babaryba']

# name_multi.append(input('Podaj jakieś imię:'))

def check_names(func):
    def hgf (name):
        if name[0].isupper():
            return  name
        return func(name)
    return hgf
    # else:
    #     pass

@check_names
def display_name(name):
    print(f'Hej, {name}')


display_name(name2)

def singleton(instance):
    created_instances = {}

    def get_instance(*args, **kwargs):
        if instance not in created_instances:
            created_instances[instance] = instance(*args, **kwargs)
        return created_instances[instance]

    return get_instance


@singleton
class OlaDuda:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
        print("Ola Duda z Krk, zielone oczy, śpiewa, lubi masło orzeczowe i myszkę Minnie ",
              self.weight, self.height)


# ola_duda_one = OlaDuda(50, 170)
# ola_duda_two = OlaDuda(40,160)

'''
Zadanie:
Skorzystaj z powyższego kodu i zmień go tak, zeby dodać jakieś indywidualne metody do Twojej osoby. W ramach ćwiczeń, 
wykorzystaj przeciążanie metody magicznej  str albo repr :wink:
'''


@singleton
class PrzPaw:
    def __init__(self, weight, height, lightsaber=None):
        self.weight = weight
        self.height = height
        self.lightsaber = lightsaber

    def give_lightsaber(self, lightsaber):
        self.lightsaber = lightsaber
        print(f'Dostałeś miecz świetlny: {self.lightsaber}')

    def __str__(self):
        return (
            f'Paweł P z Waw, o wadze: {self.weight} kg, wzroście: {self.height} cm, miecz świetlny: {self.lightsaber}')


pawel1 = PrzPaw(10, 1070)
# print(pawel1)
pawel1.give_lightsaber('blue')

# print(pawel1)
pawel1 = PrzPaw(20, 2070)
# print(pawel1)


class SingletonType(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class OlaDuda(metaclass=SingletonType):
    def __init__(self):
        print("Ola")


class SingletonClass2:
    pass


x = OlaDuda()
y = OlaDuda()

class Car(ABC):
    @abstractmethod
    def go(self):
        pass


class SportsCar(Car):
    def go(self):
        print("WROOOOOOOOOM!")


class Taxi(Car):
    def go(self):
        print("Brbrbrbrb")

class Bus(Car):
    def go(self):
        print("Prprpr")

class CarFactory(ABC):
    @abstractmethod
    def create_car(self):
        pass


class SportsFactory(CarFactory):
    def create_car(self):
        return SportsCar()


class TaxiFactory(CarFactory):
    def create_car(self):
        return Taxi()

class BusFactory(CarFactory):
    def create_car(self):
        return Bus()

car_type = 'taxi'
# car_type = input('Podaj typ pojazdu:')

if car_type == 'sport':
    factory = SportsFactory()
elif car_type == 'taxi':
    factory = TaxiFactory()
elif car_type == 'Bus':
    factory = TaxiFactory()
else:
    raise NotImplementedError(f"There is no such car like that {car_type}")

car = factory.create_car()
car.go()

'''
Zadanko:
Dodajemy inputa zamiast hardcodować plus tworzymy busy
'''



