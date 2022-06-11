def prim(n):
    s = 0
    for i in range(1,n+1):
        if n%i ==0:
            s = s+1
    if s == 2:
        return True
    else:
        return False
        
def nxt(n):
    while prim(n) == False:
        n = n+1
    return n

def beg(n):
    while prim(n)==False:
        n = n-1
    return n
    
def near(n):
    a = nxt(n)
    b = beg(n)
    if (a-n)<(n-b):
        print(a)
    else:
        print(b)
        
c = int(input())
for i in range(c):
    x = int(input())
    near(x)