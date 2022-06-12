def prim(n):
    s = 0
    for i in range(1,n+1):
        if n%i ==0:
            s = s+1
    if s==2:
        return True
    else:
        return False
        
a = int(input())
x = list(map(int,input().split()))

sum = 0

for i in x:
    if prim(i)==True :
        sum = sum+1
print(sum)