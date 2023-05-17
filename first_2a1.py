from abc import ABC, abstractmethod
class Btn(ABC):
    @abstractmethod
    def get_html(self):
        pass
class Button(Btn):
    def __init__(self):
        self.html = ""
    def get_html(self):
        return self.html
class Submit(Button):
    def __init__(self):
        super().__init__()
        self.html = "submit - wysyłanie formularz"
class Radio(Button):
    def __init__(self):
        super().__init__()
        self.html = "radio - zaznaczanie opcji"
class Check(Button):
    def __init__(self):
        super().__init__()
        self.html = "check - zaznaczanie opcji ptaszkiem"
class Clear(Button):
    def __init__(self):
        super().__init__()
        self.html = "clear - usuwa wszystkie zaznaczenia"
class ButtonFactory:
    def create_button(self,type):
        target_class = type.capitalize() # "radio" -> "Radio"
        return globals()[target_class]()
button_factory = ButtonFactory()
buttons = ['submit','radio','check','clear']
for b in buttons:
    print(button_factory.create_button(b).get_html())