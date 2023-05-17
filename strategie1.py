from abc import ABC, abstractmethod
class Strategy(ABC):
    @abstractmethod
    def execute(self, name) ->str:
        pass

class RKO(Strategy):
    def execute(self, name) ->str:
        return f"{name} is doing RKO!"

class Ambulance(Strategy):
    def execute(self, name) ->str:
        return f"{name} is calling Ambulance!"

class Default(Strategy):
    def execute(self, name) ->str:
        return f"{name} stopped and looks at the situation!"

class Police(Strategy):
    def execute(self, name) ->str:
        return f'{name} calls police.'

class Context:

    def __init__(self, name):
        self.name = name
        self.strategy = None

    def set_strategy(self, strategy = None) ->None:
        if strategy is not None:
            self.strategy = strategy
        else:
            self.strategy = Default()

    def execute_strategy(self):
        print(self.strategy.execute(self.name))


personA = Context('Ania')
personB = Context('Józio')
personC = Context('Kasia')

personA.set_strategy()
personB.set_strategy(RKO())
personC.set_strategy(Ambulance())

personD = Context('Kamil')
personD.set_strategy()
personA.set_strategy(RKO())
personD.set_strategy(Police())

personA.execute_strategy()
personB.execute_strategy()
personC.execute_strategy()
personD.execute_strategy()
