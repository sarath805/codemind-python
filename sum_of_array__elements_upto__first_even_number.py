a = int(input())
b = list(map(int,input().split()))

sum = 0        
for i in b:
    if i%2==0:
        break
    else:
        sum=sum+i
print(sum)