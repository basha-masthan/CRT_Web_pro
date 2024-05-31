roll = ["596"]
users=["Basha"]

def pp1():
    r = input("Enter your Roll Number :")
    val = input("Enter an Username :")
    if r in roll: 
        print("*********************")
        print("* User already exist *")
        print("*********************")
        pp1()
    else:  
        roll.append(r)
        users.append(val)
        print("*************")
        print("* User added *")
        print("*************")
        pp()

def pp2():
    val = input("Enter Roll Number to update :")
    if val in roll:
        key = users[roll.index(val)]
        uval = input("Enter Value to update User :")
        users[roll.index(val)] = uval
        print("**************")
        print("* User updated *")
        print("**************")
    else:
        print("*********************")
        print("* User does not exist *")
        print("*********************")
    pp()

def pp3():
    val = input("Enter Roll Number to delete :")
    if val in roll:
        users.pop(roll.index(val))
        roll.pop(roll.index(val))
        print("**************")
        print("* User deleted *")
        print("**************")
    else:
        print("**********************")
        print("* User does not exist *")
        print("**********************")
    pp()

def pp4():
    print("**************")
    print("* User List *")
    print("**************")
    for i in range(len(roll)):
        print(roll[i]+"\t"+users[i])
    print("++++++++++++++++++++++++++")
    pp()

def pp():
    try:
        p = int(input("1-> Insert a new username\n2-> Update\n3-> Delete\n4-> display :"))
    except:
        print("Invalid Input")
        pp()

    if p == 1:
        pp1()
    elif p == 2:
        pp2()
    elif p == 3:
        pp3()
    elif p == 4:
        pp4()
    elif p == 0:
        print("Exiting ...")
        exit()
    else:
        print("Invalid Input")
        pp()
pp()


