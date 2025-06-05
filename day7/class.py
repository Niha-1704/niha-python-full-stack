class Animal:
    def eating(self):
        print("Eating")
    def sound(self,r):
        print(f"some sounds {r}")
a = Animal()
a.eat = "food"
print(a.eat)
del a.eat
a.eating()
a.sound("bow bow")


class Student:
    name = ""
    roll = 0
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
        print(f"{self.name} has rollnumber {self.roll}")
    def change_name(self,new_name):
        self.name = new_name
    def show(self):
        print(f"The name changed is {self.name}")
    def display(self):
        print(f"{self.name} has {self.roll} rollnumber")
#x = Student()
#x.name = "Niha"
#x.roll = 104
#x.display()
y = Student("Deepu", 575)
y.change_name("lavanya")
y.show()
y.display()