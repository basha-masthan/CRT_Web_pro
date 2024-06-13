def p1():
    print("Hello world!")
# 1'st Py Program
# p1()


def p2():
    a = int(100)
    b = int("200")
    print(a+b)
# 2'nd Py Program
# p2()

def p3():
    a=100
    print("a =",a)
    print("Type of a :",type(a))
    a= "Basha"
    print("a =",a)
    print("Type of a :",type(a))
# 3'rd Py Program
# p3()

def p4():
   k = input("Enter a Value: ")
   print(k)
# p4()

def p5(): 
    a = int(input("Enter a Value: "))
    b = int(input("Enter b Value: "))
    print("a + b :",a+b)
    print("a - b :",a-b)
    print("a * b :",a*b)
    print("a / b :",a/b)
    print("a // b :",a//b)
    print("a % b :",a%b)
    print("a ** b :",a**b)

# p5()

def p6():
    a = int(input("Enter a values: "))
    b = int(input("Enter b values: "))
    print("a > b :",a>b)
    print("a < b :",a<b)
    print("a == b :",a==b)
    print("a!= b :",a!=b)
    print("a >= b :",a>=b)
    print("a <= b :",a<=b)
# p6()

 
def p7():
    a = int(input("Enter a Value: "))
    b = int(input("Enter b Value: "))
    if(a > b):
        print("a is grater than b")    
    elif(a < b):
        print("b is grater than a")
    else:
        print("a is equal to b")
# p7()

def p8():
    a = int(input("Enter a Value: "))
    b = int(input("Enter b Value: "))
    c = int(input("Enter c Value: "))
    if(a > b and a > c):
        print("a is grater than b and c")
    elif(a == b and a>c):
        print("a,b is grater than c")
    elif(a ==c and a>b):
        print("a,c is grater than b")
    elif(b > c and b > c):
        print("b is grater than a and c")
    elif(b == c and b>a):
        print("b,c is grater than a")
    elif(c == a and c>b):
        print("c,a is grater than b")
    elif(c > b and c > b):
        print("c is grater than a and b")
    elif(c == b and c>a):
        print("c,b is grater than a")
    elif(c == a and c>b):
        print("c,a is grater than b")
    else:
        print("All are equal")
# p8()

def p9():
    k = input("Enter a string :")
    print(k[0])

# p9()


def p10():
    k = input("Enter a string :")
    k = k.lower();
    q = ['a','e','i','o','u']
    if( k[0] in q):
        print("Vowel")
    else:
        print("Consonant")
p10()
