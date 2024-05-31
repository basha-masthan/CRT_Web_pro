admin = "basha"
a_pass = "king"

user = []
pass = []

data = {}

def std_login():
    print("**********")
    print("* Login *")
    print("**********")
    u = input("Enter Username :")
    p = input("Enter Password :")
    if u == admin and p == a_pass:
        print("**************")
        print("* Login Successfull *")
        print("**************")
        usr_menu()
    else:
        print("**************")
        print("* Login Failed *")
        print("**************")
        usr_login()

def admin_login():
    print("**********")
    print("* Login *")
    print("**********")
    u = input("Enter Username :")
    p = input("Enter Password :")
    if u == admin and p == a_pass:
        print("**************")
        print("* Login Successfull *")
        print("**************")
        admin_menu()
    else:
        print("**************")
        print("* Login Failed *")
        print("**************")
        admin_login()

def usr_menu():
    print("**********")
    print("* User Menu *")
    print("**********")
    print("1. Admin Login")
    print("2. Student Login")
    print("0. Exit")
    try:
        p = int(input("Enter Choice :"))
    except:
        print("Invalid Input")
        usr_menu()
    if p == 1:
        admin_login()
    elif p == 2:
        std_login()
    elif p == 0:
        print("Exiting ...")
        exit()
    else:
        print("Invalid Input")
        usr_menu()


def admin_menu():
    print("**********")
    print("* Admin Menu *")
    print("**********")
    print("1. Add User")
    print("2. Update User")
    print("3. Delete User")
    print("4. Display User")
    print("0. Exit")
    try:
        p = int(input("Enter Choice :"))
    except:
        print("Invalid Input")
        admin_menu()
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
        admin_menu()

def std_menu():
    print("***********")
    print("* Student Menu *")
    print("***********")
    print("1. Fee balance")
    print("2. Grade Score")
    print("3. Backlog check")
    print("4. Attendance Percentage")
    print("0. Exit")
    try:
        p = int(input("Enter Choice :"))
    except:
        print("Invalid Input")
        std_menu()
    if p == 1:
        std_fee()
    elif p == 2:
        std_grade()
    elif p == 3:
        std_backlog()
    elif p == 4:
        std_attendance()
    elif p == 0:
        print("Exiting ...")
        exit()
    else:
        print("Invalid Input")
        std_menu()


def Add_grade_score():
    print("***********")
    print("* Add Grade Score *")
    print("***********")
    try:
        g = int(input("Enter Roll :"))
    except:
        print("Invalid Input")
        Add_grade_score()
    if g > 100 or g < 0:
        print("Invalid Input")
        Add_grade_score()
    else:
        if()
        print("***********")
        print("* Grade Score Added *")
        print("***********")
    std_menu()


def std_grade():
    print("***********")
    print("* Grade Score *")
    print("***********")