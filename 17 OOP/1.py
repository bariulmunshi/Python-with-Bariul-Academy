"""
class Student:
    #Attributes
    name=""
    age=0
    gender=""
    #Methods
    def set_info(self):
        self.name=input("Enter name: ")
        self.age=int(input("Enter age: "))
        self.gender=input("Enter gender: ")

    def display(self): 
        #print("This is a display method")
        print(f"My name is {self.name}, age is {self.age} and gender is {self.gender}")

s1=Student()
s1.set_info("Alice", 20, "Female")
s1.display()

s2=Student()
s2.set_info()
s2.display()    
"""
class Student:
    #Attributes
    name=""
    age=0       
    gender=""
    #Methods
    def set_info(self, n, a, g):
        self.name=n
        self.age=a
        self.gender=g
    def display(self): 
        print(f"My name is {self.name}, age is {self.age} and gender is {self.gender}")
s1=Student()
s1.set_info ("Alice", 20, "Female")
s1.display()
