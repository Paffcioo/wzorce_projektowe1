#Klasa do zaadaptowania
class UglyWoman:
    def request_for_pretty(self):
        return "I am ugly. I want to be prettier."


# target - klasa do jakiej musimy dopasować powyższą klasę (nasz cel)
class PrettyWoman:
    def request_for_pretty_change(self):
        return "\n Target: being pretty woman."

#adapter - klasa, która zajmie się adaptacją klasy do zaadaptowania do klasy targetowej
class MakeUp(UglyWoman, PrettyWoman):
    def request(self):
        return f"\n Makeup (person change): {self.request_for_pretty_change()[::-1]}"

class Exercises(UglyWoman, PrettyWoman):
    def request(self):
        return f"\n Exercises: {self.request_for_pretty_change()[::-1]}"

# To nie musi byc
# def client_code(woman):
#     print(woman.request(), end="")

#Chcemy być ładni
target = PrettyWoman()
target.request_for_pretty_change()

#Ale na arzie ejsteśmy brzydcy
adaptee = UglyWoman()
print(f"Client: Adaptee class has a weir interface - she is ugly right now.", end="\n")
print(f"Adaptee: {adaptee.request_for_pretty()}", end="\n")

print("Client: I can work with adapter. I need smth to make this woman prettier.")
adapter = MakeUp()
print(adapter.request())
# client_code(adapter)

adapter2 = Exercises()
print(adapter2.request())
# client_code(adapter2)