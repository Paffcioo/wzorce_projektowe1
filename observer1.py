posts = []

class InstaSubscriber:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f'{self.name} sees post: {message}')

    def response(self, post_number, comment):
        print(f'{self.name} commented post: {posts[int(post_number)]} saying: {comment}')

class Influencer:
    def __init__(self):
        self.subscribers = set()

    def register(self, who):
        self.subscribers.add(who)

    def unregister(self, who):
        self.subscribers.discard(who)

    def dispatch(self, post):
        for subscriber in self.subscribers:
            subscriber.update(post)
        posts.append(post)

beyonce = Influencer()

obs1 = InstaSubscriber('Kasia')
obs2 = InstaSubscriber('Adam')
obs3 = InstaSubscriber('Krzysztof')
obs4 = InstaSubscriber('Zenon')

print('Beyonce new followers:')

beyonce.register(obs1)
beyonce.register(obs2)
beyonce.register(obs3)
beyonce.register(obs4)

print('Beyonce is adding new post.')

beyonce.dispatch('Welcome my fans!')

beyonce.unregister(obs1)

print('Beyone 2nd post:')

beyonce.dispatch('I love you!')

obs4.response(1, 'Good!')
obs3.response(1, 'It was a bad idea!')
beyonce.unregister(obs3)

beyonce.dispatch('This is my dominion!')

print(posts)