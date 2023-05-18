class InstaSubscriber:
    def __init__(self, name):
        self.name = name

    def update(self,message):
        print(f"{self.name} sees post ====> {message}")

    def view_story(self, story, influencer_name):
        print(f"\33[21m{self.name}\33[0m viewed \33[34m{influencer_name}'s\33[0m story titled '{story}'")


class Influencer:
    def __init__(self, name):
        self.subscribers = set()
        self.name = name

    def register(self, who):
        self.subscribers.add(who)
        print(who.name)

    def unregister(self,who):
        self.subscribers.discard(who)
        print(who.name)

    def dispatch(self,post):
        for subscriber in self.subscribers:
            subscriber.update(post)

    def story(self, story):
        for subscriber in self.subscribers:
            subscriber.view_story(story, self.name)


#tworzenie kont na insta

beyonce = Influencer('Beyonce')

obs1 = InstaSubscriber('Kasia')
obs2 = InstaSubscriber('Adam')
obs3 = InstaSubscriber('Jacek')

print(f"\n{beyonce.name} new followers:")
beyonce.register(obs1)
beyonce.register(obs2)
beyonce.register(obs3)

print(f"\n{beyonce.name} is adding new post:")
beyonce.dispatch(f'Hello guys!')

print(f"\n{beyonce.name} is lost follower(s):")
beyonce.unregister(obs2)

print(f"\n\33[45m{beyonce.name} is adding new story:\33[0m")
beyonce.story(f'New video from my last performance')