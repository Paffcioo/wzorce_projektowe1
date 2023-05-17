class Button:
    html = ""

    def get_html(self):
        return self.html

class Submit(Button):
    html = "submit - wysyłanie formularza"

class Radio(Button):
    html="radio - zaznaczanie opcji"

class Check(Button):
    html= "check - zaznaczanie opcji ptaszkiem"

class Reset(Button):
    html= "reset - kasowanie danych"

class ButtonFactory:
    def create_button(self,type):
        target_class = type.capitalize() # "radio" ==> "Radio"
        return globals()[target_class]()


button_factory = ButtonFactory()

buttons = ['submit', 'radio', 'check', 'reset']

for b in buttons:
    print(button_factory.create_button(b).get_html())