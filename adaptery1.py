#klasa do zaadaptowania
class UglyWomen:
    def request_for_pretty(self):
        return " I am ugly! I want to be priettier!"

#target - czyli klasa do jakiej musimy dopasować powyższą klasę, to jest nasz cel - bycie ładną!
class PrettyWomen:
    def request_for_pretty_change(self):
        return "\n Target: Being pretty woman!!!"

#adapter - klasa, która zajmie się adaptacją klasy do zaadaptowania do klasy targetowej
class MakeUp(UglyWomen, PrettyWomen):
    def request(self):
        return f'\n Makeup (person change): {self.request_for_pretty_change()[::-1]}'
    def request_for_removal(self):
        return f'\n Removing makeup {self.request_for_pretty_change()*2}'


def client_code(woman):
    print(woman.request_for_removal(), end="")

#chcemy być ładni
target = PrettyWomen()
target.request_for_pretty_change()

# ale teraz narazie jesteśmy brzydcy
adaptee = UglyWomen()
print(f"Client: Adaptee class has a weir interface - she is ugly right now", end="\n")
print(f"Adaptee:{ adaptee.request_for_pretty()}", end="\n")

print("Client: I can work with adapter!!! I need some magic to make a woman prettier :)")
adapter = MakeUp()
print(adapter.request())
client_code(adapter)
# print(adapter.request_for_removal())
