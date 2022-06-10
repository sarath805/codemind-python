def reve(n):
    s = 0
    while n>0:
        r = n%10
        s = s*10+r
        n =n//10
    return s
    
a = int(input())
s = a**2
b = reve(a)
c = b**2
e = reve(c)

if s==e:
    print(True)
else:
    print(False)