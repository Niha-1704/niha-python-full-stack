class Student:
    name = ""
    roll = 0
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
        #print(f"{self.name} has rollnumber {self.roll}")
    def __str__(self):
        return f"{self.name} has {self.roll}"
    def display(self):
        print(f"{self.name} has {self.roll} rollnumber")
y = Student("Deepu", 575)
#y.display()
print(y)