def fun(n):
    s = ''
    for i in range(n):
        s += '*'
        yield s


for x in fun(3):
    print(x, end='')
