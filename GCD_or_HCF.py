a,b = map(int,input().split())
sum = 0
for i in range(1,b+1):
    if (a*i)%b==0:
        sum = sum+(a*i)
        break
    
g = ((a*b)//sum)

print(g)