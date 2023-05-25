from abc import ABC, abstractmethod


class ChosenSide(ABC):
    @abstractmethod
    def make_choice(self, name) -> str:
        pass


class LightSide(ChosenSide):
    def make_choice(self, name) -> str:
        return f'\33[32m{name} is following the Path of Light\33[0m'


class DarkSide(ChosenSide):
    def make_choice(self, name) -> str:
        return f'\33[31m{name} is turing into the Dark Side\33[0m'


class Grey(ChosenSide):
    def make_choice(self, name) -> str:
        return f"\33[31m{name} sees ambiguity of the situation\33[0m"


class Abandon(ChosenSide):
    def make_choice(self, name) -> str:
        return f'\33[35m{name} is abandoning the Jedi Path\33[0m'


class Padawan:
    def __init__(self, name, midichlorians, gender=None):
        self.name = name
        self.midichlorians = midichlorians
        self.gender = gender
        self.skills = set()
        self.chosen_side = None
        self.master = None

    def assign_to_master(self, master):
        self.master = master
        print(f'{self.name} with {self.midichlorians} was assigned to {master}', )

    # def display_master(self):
    #     return self.master
    #
    # def who_stronger(self):

    def learn_new_skill(self, skill, master):
        self.skills.add(skill)
        if self.gender == 'female':
            print(f'\n{self.name} learned {skill} skill from her Jedi Master {master}')

        elif self.gender == 'male':
            print(f'\n{self.name} learned {skill} skill from his Jedi Master {master}')

        elif self.gender is None:
            print(f'\n{self.name} learned {skill} skill from its Jedi Master {master}')

    def show_skills(self):
        print(f'Padawan {self.name} has following set of skills: {self.skills}')

    def choose_side(self, other, chosen_side = None) -> None:
        if chosen_side is not None:
            self.chosen_side = chosen_side
        else:
            if self.midichlorians <= other.midichlorians:
                self.chosen_side = LightSide()
            elif self.midichlorians > other.midichlorians:
                self.chosen_side = DarkSide()

    def display_side(self):
        print(self.chosen_side.make_choice(self.name))


class JediMaster:
    def __init__(self, name, midichlorians, lightsaber, skill):
        self.name = name
        self.midichlorians = midichlorians
        self.lightsaber = lightsaber
        self.skill = skill
        self.padawans = list()

    def loose_padawan(self, padawan):
        self.padawans.remove(padawan)

    def teach_skill(self, skill=None):
        if skill is None:
            skill = self.skill
        for padawan in self.padawans:
            padawan.learn_new_skill(skill, self.name)

    def accepot_new_padawan(self, padawan):
        self.padawans.append(padawan)

    def show_padawans(self):
        print(f'\nJedi Master {self.name} trains {len(self.padawans)} following padawans:')
        for padawan in self.padawans:
            print(padawan.name, end=",")

jedi1 = JediMaster('Alex', 10_000, 'blue', 'force jump')
jedi2 = JediMaster('Obi Two', 4_000, 'yellow', 'force pull')
jedi3 = JediMaster('Qasim', 6_000, 'green', 'battle meditation')

padawan1 = Padawan('Anakin', 20_000, 'male')
padawan2 = Padawan('Oya', 13_500, 'female')
padawan3 = Padawan('Lego', 11_000)
padawan4 = Padawan('Lando', 8_500, 'male')
padawan5 = Padawan('Nela', 9_000, 'female')
padawan6 = Padawan('Jake', 10_000, 'male')
padawan7 = Padawan('Orto', 12_000)

jedi1.accepot_new_padawan(padawan1)
jedi2.accepot_new_padawan(padawan2)
jedi3.accepot_new_padawan(padawan3)
jedi1.accepot_new_padawan(padawan4)
jedi2.accepot_new_padawan(padawan5)
jedi3.accepot_new_padawan(padawan6)
jedi1.accepot_new_padawan(padawan7)

jedi1.show_padawans()
jedi2.show_padawans()
jedi3.show_padawans()

jedi1.teach_skill()
jedi2.teach_skill()
jedi2.teach_skill('Lighgtnings')
jedi3.teach_skill()
padawan2.show_skills()
padawan1.show_skills()

padawan1.choose_side(jedi1)
padawan1.display_side()
# padawan1.choose_side(DarkSide())
padawan1.display_side()

print(padawan1.master())

