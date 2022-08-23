def prime(n):
    s = 0
    for i in range(1,n+1):
        if n%i == 0:
            s = s+1
    if s == 2:
        return True
    else:
        return False

a = int(input())
b = int(input())
for i in range(a,b+1):
    if prime(i) == True:
        print(i)