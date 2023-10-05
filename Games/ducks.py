class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Wee, this is fun.")
        elif self.ratio == 1:
            print("This is hard work, but I'm flying.")
        else:
            print("I think I'll just walk.")


class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print("Waddle, waddle, waddle")

    def swim(self):
        print("Come on in, the water's lovely")

    def quack(self):
        print("Quack quack")

    def fly(self):
        self._wing.fly()


class Penguin(object):

    def walk(self):
        print("Waddle, waddle, I waddle too")

    def swim(self):
        print("Come on in, but it's a bit chilly this far South")

    def quack(self):
        print("Are you having a laugh? I'm a penguin!")


class Flock(object):

    def __init__(self):
        self.flock = []
# In the following we added hints to the add_duck method. The hints lets
# anyone using the add_duck module understands what they should be providing
# to the method.  We added annonation Inside the paratheses of the method we
# added a parameter, duck.

    def add_duck(self, duck: Duck) -> None:
        self.flock.append(duck)

    def migrate(self):
        for duck in self.flock:
            duck.fly()


if __name__ == '__main__':
    donald = Duck()
    donald.fly()
