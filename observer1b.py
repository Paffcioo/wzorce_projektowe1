class InstaSubscriber:
    def __init__(self, name):
        self.name = name

    def update(self,message):
        print(f"{self.name} sees post ====> {message}")

    def reply(self, post, reaction):
        print(f"{self.name} replied with {reaction}")

class Influencer:
    def __init__(self):
        self.subscribers = set()

    def register(self,who):
        self.subscribers.add(who)

    def unregister(self,who):
        self.subscribers.discard(who)

    def dispatch(self, post):
        flag = True
        for subscriber in self.subscribers:
            subscriber.update(post)
            if flag:
                subscriber.reply(post, "like")
                flag = False
            else:
                subscriber.reply(post, "heart")
                flag = True




#tworzenie kont na insta

beyonce = Influencer()

obs_1 = InstaSubscriber("Kasia")
obs_2 = InstaSubscriber("Adam")
obs_3 = InstaSubscriber("Krzyś")
obs_4 = InstaSubscriber("Maciek")


#dokonujemy subskrypcji beyonce
print("Beyonce new followers")
beyonce.register(obs_1)
beyonce.register(obs_2)
beyonce.register(obs_3)
beyonce.register(obs_4)


print("Beyonce is adding new post")
beyonce.dispatch("Welcome my fans! I love you!!! <3")

beyonce.unregister(obs_2)

print("Beyonce is adding next new post")
beyonce.dispatch("I am going on tour!")