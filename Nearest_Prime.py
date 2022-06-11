def prin(n):
    s = 0
    for i in range(1,n+1):
        if n%i == 0:
            s = s+1
    if s == 2:
        return True
    else:
        return False
        
def bef(n):
    while prin(n) ==False:
        n = n-1
    return n
def nxt(n):
    while prin(n)==False:
        n = n+1
    return n
    
def near(n):
    x = bef(n)
    y = nxt(n)
    
    if (n-x)<=(y-n):
        print(x)
    else:
        print(y)

a = int(input())
for i in range(a):
    b = int(input())
    near(b)