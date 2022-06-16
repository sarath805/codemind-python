def prime(n):
    sum = 0
    for i in range(1,n+1):
        if n%i == 0:
            sum = sum+1
            
    if sum == 2:
        return True
    else:
        return False
        
a = int(input())
x = list(map(int,input().split()))
c = 0
for i in x:
    if prime(i) == True :
        c = c+1
        
print(c)