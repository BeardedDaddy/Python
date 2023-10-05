class Player(object):

    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0

    def _get_lives(self):
        return self._lives
    
    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives cannot be negative.")
            self._lives = 0

    def _get_level(self):
        return self._level
    
    def _set_level(self, level):
        if level > 0:
            delta = level - self._level
            self._score += delta * 1000
            self._level = level
        else:
            print("Level can't be less than 1")
    # Create a function that to where the player's scores are increased by one thousand every time their level increases by one.
    # So if they jump up two levels, they'll get a bonus of two thousand added to their score.
    # If the player drops back a level, they'll lose one thousand for each level they drop back.
    # They can't go below a level One, so the solution should prevent that from happening.
    # Use properties to create this function.
    
    lives = property(_get_lives, _set_lives)
    level = property(_get_level, _set_level)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score: {0.score}".format(self)
