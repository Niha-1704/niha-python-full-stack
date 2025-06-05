class Animal:
    pass
class Dog(Animal):
    def sound(self):
        print("Bow Bow")
class Cat(Animal):
    def sound(self):
        print("Meow Meow")
a = [Dog(),Cat()]
for i in a:
    i.sound()