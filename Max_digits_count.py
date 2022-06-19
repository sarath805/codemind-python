a = int(input())
x = list(map(str,input().split(' ')))
z = []

for i in x:
    z.append(len(i))
    
m = max(z)
sum = 0

for j in x:
    if len(j) == m:
        sum = sum+1
        
print(sum)