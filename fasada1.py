class Hug:
    def do_it(self):
        print('Give her million hugs!')


class Blanket:
    def do_it(self):
        print('Give her a blanket.')


class Feed:
    def do_it(self):
        print('Omnomnom Food!')


class Sleep:
    def do_it(self):
        print('Hrrr... zzz...')


class GreenTea:
    def do_it(self):
        print('Gulp!')

class Movie:
    def do_it(self):
        print('Watching, watching...')


class PeriodAction:
    def __init__(self):
        self.feed = Feed()
        self.hug = Hug()
        self.movie = Movie()
        self.blanket = Blanket()
        self.sleep = Sleep()
        self.tea = GreenTea()

    def start_period_action(self):
        self.hug.do_it()
        self.feed.do_it()
        self.tea.do_it()
        self.blanket.do_it()
        self.movie.do_it()
        self.sleep.do_it()


period_time = PeriodAction()
period_time.start_period_action()
