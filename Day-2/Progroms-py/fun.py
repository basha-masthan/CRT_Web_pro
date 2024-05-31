users=[]
roll = []

def pp1():
    r = input("Enter your Roll Number")
    val = input("Enter an Username ")
    if r in roll: 
        print("Username already exists")
        pp1()
    else:  
        roll.append(r)
        users.append(val)
        print(users)
        pp()

def pp2():
    val = input("Enter Roll Number to update")
    if val in roll:
        key = users[roll.index(val)]
        uval = input("Enter Value to update User ")
        users[roll.index(val)] = uval
        print(users)
    pp1()

def pp3():
    print("PP3")

def pp4():
    print("PP4")
    pp3()

def pp():
    p = int(input("1-> Insert a new username\n2-> Update\n3-> Delete\n4-> display :"))
    if p == 1:
        pp1()
    elif p == 2:
        pp2()
    elif p == 3:
        pp3()
    elif p == 4:
        pp4()
    else:
        print("Invalid Input")
        pp()
pp()


