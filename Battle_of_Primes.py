def prime(n):
    s = 0
    for i in range(1,n+1):
        if n%i == 0:
            s = s+1
    if s==2:
        return True
    else:
        return False
        
n1 = int(input())
n2 = int(input())
b = n1+n2
a = n1+n2
while a>0:
    a = a+1
    if prime(a) == True:
        print(a-b)
        break
    else:
        continue
        