class InstaSubscriber:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f'{self.name} see post ===> {message}')

    def update_name(self, new_name):
        self.name = new_name


class Influencer:
    def __init__(self):
        self.subscribes = set()
        self.posts = dict()

    def register(self, who):
        self.subscribes.add(who)

    def unregister(self, who):
        self.subscribes.discard(who)

    def dispatch(self, post):
        for subscriber in self.subscribes:
            subscriber.update(post)
        self.posts[post] = len(self.subscribes)

    def show_posts(self):
        for post, num in self.posts.items():
            print(f"The post '{post}' viewed by {num} observers")

# Tworzenie konta na insta
beyonce = Influencer()

obs1 = InstaSubscriber("Adam")
obs2 = InstaSubscriber("Kasia")
obs3 = InstaSubscriber('Seba')
obs4 = InstaSubscriber('Alan')

# dokonujemy subskrypcji Beyonce
print("Beyonce new followers")
beyonce.register(obs1)
print(obs1.name)
beyonce.register(obs2)
print(obs2.name)
beyonce.register(obs3)
print(obs3.name)
beyonce.register(obs4)
print(obs4.name)

print("Beyonce add new post")
beyonce.dispatch("Hello my friends!!!")

beyonce.unregister(obs1)
beyonce.dispatch("I am going to Great Wall in China")

obs3.update_name('Sebastian')

beyonce.register(obs1)
beyonce.dispatch('Show time')

# Wyświetlenie wszystkich postów
beyonce.show_posts()