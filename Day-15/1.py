class man:
    def __init__(p):
        p.name = input("Enter Name :")
        p.age = int(input("Enter Age :"))
        p.grade = float(input("Enter Grade :"))
        print("Constructor...")

e = man()

print("Std Name :",e.name)
print("Std Age :",e.age)
print("Std Grade :",e.grade)
