import pickle
import json


class Fruit:
    def __init__(self, name: str, calories: float):
        self.name = name
        self.calories = calories

    def describe_fruit(self):
        print(self.name, self.calories, sep=': ')


if __name__== '__main__':
    fruit: Fruit = Fruit('Banana', 100)
    fruit.describe_fruit()

    fruit.calories = 150
    
    with open('banana.json', 'w')
    
    