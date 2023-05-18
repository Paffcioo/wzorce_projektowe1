from abc import ABCMeta, abstractmethod


class IOs(metaclass=ABCMeta):
    "The Operating System Abstraction Interface"

    @staticmethod
    @abstractmethod
    def operate():
        "will be overridden in implementer"


class IOsImplementer(metaclass=ABCMeta):
    "Os Implementer"

    @staticmethod
    @abstractmethod
    def operate_implement():
        """"""


class Linux(IOs):

    def __init__(self, implementer):
        self.implementer = implementer()

    def operate(self):
        self.implementer.operate_implement()


class Windows(IOs):

    def __init__(self, implementer):
        self.implementer = implementer()

    def operate(self):
        self.implementer.operate_implement()


class LinuxImplementer(IOsImplementer):

    def operate_implement(self):
        print("Sudo!")


class WindowsImplementer(IOsImplementer):

    def operate_implement(self):
        print("Windows!")


w = Windows(WindowsImplementer)
w.operate()
l = Linux(LinuxImplementer)
l.operate()