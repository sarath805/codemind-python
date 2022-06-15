a = int(input())
x = list(map(int,input().split()))
sum = sum2 = 0 
for i in x:
    a = x.index(i)
    if a%2 != 0 and i%2 != 0:
        sum = sum +1
    if i%2 != 0:
        sum2 = sum2+1
        
if sum == sum2:
    print(True)
else:
    print(False)