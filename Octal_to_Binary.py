a = int(input())
for i in range(a):
    x = input()
    k = int(x,8)
    b = bin(k)
    l = list(b)
    l.pop(0)
    l.pop(0)
    s = ' '
    for i in l:
        s = s+i
    print(int(s))