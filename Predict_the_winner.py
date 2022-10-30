a = int(input())
x = list(map(int,input().split()))
e = 0
o = 0
for i in x:
    p = x.index(i)
    if p%2 == 0:
        e = e+i
    else:
        o = o+i
d = abs(e-o)
if d%4 == 0:
    print("X")
else:
    print("Y")