#single inheritance
# class Animal:
#     type =""
#     def sound(self):
#         print("Some Sound")
# class Dog(Animal):
#     def dog_s(self):
#         print("Bow bow")
# #a = Animal()
# #a.sound()
# b = Dog()
# b.sound()
# b.dog_s()

#multiple inheritance
# class Cat():
#     name = ""
#     def cat_s(self):
#         print("Meow Meow")
# class carnivor(Dog,Cat):
#     def show(self):
#         print("carnivorous animals")
# a = Cat()
# a.name = "cat"
# c = carnivor()
# c.dog_s()
# c.cat_s()
# c.show()

#multilevel
# class Animal:
#     def display(self):
#         print("Animals")
# class King(Animal):
#     def show(self):
#         print("I am the king Mufasa")
# class Simba(King):
#     def fut_king(self):
#         print("I am the next king Simba")
# s = Simba()
# s.display()
# s.show()
# s.fut_king()

#hierarchical
# class Livingthings:
#     pass
# class Bird(Livingthings):
#     def show(self):
#         print("Birds is a Living Thing")
# class Animal(Livingthings):
#     def display(self):
#         print("Animals is a Living Thing ")
# b = Bird()
# b.show()
# a = Animal()
# a.display()

#Hybrid inheritance
class Grandparent:
    pass
class Parent(Grandparent):
    def display(self):
        print("parents..")
class Bro(Parent):
    def show(self):
        print("i am her brother. we are siblings")
class Sis(Parent):
    def dis(self):
        print("I am his sister.we are siblings.")
b = Bro()
b.display()
b.show()
s = Sis()
s.display()
s.dis()