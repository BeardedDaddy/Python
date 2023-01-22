class Player(object):
<<<<<<< HEAD
    def __init__(self, name):
        self.name = name
        self._lives = 3
=======

    def __init__(self, name):
        self.name = name
        self.lives = 3
>>>>>>> d8d76de5c5eaf5716245077a1bd736626a24dd52
        self.level = 1
        self.score = 0

    def _get_lives(self):
<<<<<<< HEAD
        return self._lives
    
    def _set_lives(self, lives):
        if lives >= 0:
            set._lives = lives
        else:
            print("Lives cannot be negative.")
            set._lives = 0

    lives = property(_get_lives, _set_lives)

    def __self__(self):
        return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score: {0.score}".format(self)
        
=======
        return self.lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives cannot be negative")
            self._lives = 0

    lives = property(_get_lives, _set_lives)

    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score: {0.score}".format(self)
>>>>>>> d8d76de5c5eaf5716245077a1bd736626a24dd52
