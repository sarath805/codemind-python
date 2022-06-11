def prim(n):
    s = 0
    for i in range(1,n+1):
        if n%i==0:
            s = s+1
    if s==2:
        return True
    else:
        return False
        
def nxt(n):
    while prim(n)==False:
        n = n+1
    return n
def bef(n):
    while prim(n)==False:
        n = n-1
    return n
    
def near(n):
    a = nxt(n)
    b = bef(n)
    if (a-n)<(n-b):
        print(abs(n-a))
    else:
        print(abs(n-b))
        
h = int(input())
near(h)