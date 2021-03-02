class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print(self.name + ' is walking....')
    
    def speak(self):
        print('Hello my name is ' + self.name + ' and I am ' + str(self.age) + ' years old ')

Grevy = Person('Grevy', 48)

Grevy.speak()
Grevy.walk()

print('-----------')

Tammie = Person('Tammie', 47)
Tammie.speak()
Tammie.walk()
