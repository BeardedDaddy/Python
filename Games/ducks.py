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

    def __init__(self):
        self.fly = self.aviate

    def walk(self):
        print("Waddle, waddle, I waddle too")

    def swim(self):
        print("Come on in, but it's a bit chilly this far South")

    def quack(self):
        print("Are you having a laugh? I'm a penguin!")

    def aviate(self):
        print("I won the lottery and bought a learjet")


class Mallard(Duck):
    pass


class Flock(object):

    def __init__(self):
        self.flock = []
# In the following we added hints to the add_duck method. The hints lets
# anyone using the add_duck module understands what they should be providing
# to the method.  We added annonation Inside the paratheses of the method we
# added a parameter, duck.

    def add_duck(self, duck: Duck) -> None:
        fly_method = getattr(duck, 'fly', None)
        if callable(fly_method):
            self.flock.append(duck)
        else:
            raise TypeError("Cannot add duck, are you sure it's not a " + str(type(duck).__name__))  # noqa

    def migrate(self):
        problem = None
        for duck in self.flock:
            try:
                duck.fly()
            except AttributeError as e:
                print("One duck down")
                problem = e
        if problem:
            raise problem


if __name__ == '__main__':
    donald = Duck()
    donald.fly()
