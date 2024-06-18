class std:
    pass

e1 = std()

e1.name = "Basha"
e1.age= 25
e1.Grade = 22.5


# print("Name: ",e1.name)
# print("Age: ",e1.age)
# print("Grade: ",e1.Grade)

class P1:
    def __init__(self,roll,name,age,):
        pass

# e2 = P1(12,"Basha",25)


class p2:
    def __init__(self,roll,name,age):
        self.roll = roll
        self.name = name
        self.age = age
    def display(self):
        print("Roll :",self.roll)
        print("Name :",self.name)
        print("Age :",self.age)

# kk = p2(12,"Basha",25)
# pp = p2(24,"Suku",50)
# kk.display()
# print("\n")
# pp.display()

name = []


class p3:
    def  __init__(self):
        self.name = input("Name :")
        self.age = int(input("Age :"))
        self.grade = float(input("Grade :"))
        name.append(self.name)

    def display(self):
        print("No of students :",len(name))
        for i in name:
            print(name.index(i)+1,i)
# n=0
# while n<2:
#     kk = p3()
#     n+=1
# kk.display()

class p4:
    def __init__(self):
        self.roll = int(input("Roll :"))
        self.name = input("Name :")
        self.grade = float(input("Grade :"))
    def display(self):
        print("Roll :",self.roll)
        print("Name :",self.name)
        print("Grade :",self.grade)
    
    def fun1():
        print("Function in class")
    def fun2(cls):
        print("Function in class")
    def __del__(self):
        print("Destructor") 

# pp4 = p4()
# pp4.display()

# p4.fun1()


class parent:
    def __init__(self) :
        self.a = int(input("a :"))
        self.b= int(input("b :"))

class child(parent):
    def __init__(self):
        parent.__init__(self)
        self.c = int(input("c :"))
        self.d = int(input("d :"))

    def add(self):
        print("C + D :",self.c+self.d)
        print("A + B :",self.a+self.b)

c1 = child()
``4
c1.add()
    



    