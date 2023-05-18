class Memento:
    def __init__(self, person, period):
        self.person = person
        self.period_of_lifespan = period


class Person:
    def __init__(self, name):
        self.name = name
        self.period_of_lifespan = ""

    def save(self):
        return Memento(self.name, self.period_of_lifespan)

    def undo(self, memento):
        self.name = memento.person
        self.period_of_lifespan = memento.period_of_lifespan

    def period_in_life(self, period):
        self.period_of_lifespan = period


class Alzheimer:
    def save(self, writer):
        self.obj = writer.save()

    def undo(self, writer):
        writer.undo(self.obj)


caretaker = Alzheimer()

person = Person("Karol")
person.period_in_life("childhood")

print("When {name} was 7 years old, he remembers: {period}".format(name=person.name, period=person.period_of_lifespan))

caretaker.save(person)

person.period_in_life("adolescence (including childhood)")
print("When {name} was 30 years old, he remembers: {period}".format(name=person.name, period=person.period_of_lifespan))

caretaker.undo(person)

print("When {name} was 60 years old, he remembers: {period}".format(name=person.name, period=person.period_of_lifespan))