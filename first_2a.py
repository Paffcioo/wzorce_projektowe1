
class MinnieMouse:
    def __init__(self):
        self.translations = {"pl": "Myszka Minnie", "en": "Minnie Mouse"}

    def localize(self, msg):
        '''
        The get method of a dictionary in Python returns
        the value associated with a key.
        If the key is not found in the dictionary,
        it returns a default value specified as the second argument,
        in this case msg.
        '''
        return self.translations.get(msg, msg)


class Snowman:
    def __init__(self):
        self.translations = {"pl": "Bałwan", "en": "Snowman"}

    def localize(self, msg):
        """
        The get method of a dictionary in Python returns the value
        associated with a key. If the key is not found in the dictionary,
        it returns a default value specified as the second argument,
        in this case msg.
        """
        return self.translations.get(msg, msg)


def factory(language='en'):
    localizers = {
        "Minnie": MinnieMouse,
        "Snowman": Snowman
    }

    return localizers[language]()


if __name__ == '__main__':

    message = ["pl", "en"]

minnie = factory("Minnie")
snowman = factory("Snowman")

# TODO - zmienić tak pętle, żeby dynamicznie iterować po obiektach
for msg in message:
    print(minnie.localize(msg))
    print(snowman.localize(msg))
