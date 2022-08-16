for i in range(int(input())):
    x = int(input())
    b = bin(x)
    c = list(b)
    c.pop(0)
    c.pop(0)
    k =' '
    for i in c:
        k = k+i
    print(int(k))