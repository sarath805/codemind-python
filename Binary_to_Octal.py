for i in range(int(input())):
    x = input()
    n = int(x,2)
    p = oct(n)
    o = list(p)
    o.pop(0)
    o.pop(0)
    s = ' '
    for i in o:
        s = s+i
    print(int(s))