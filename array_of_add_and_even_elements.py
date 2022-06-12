a = int(input())
x = list(map(int,input().split()))
z = []

for i in x:
    if i%2 != 0:
        z.append(i)
        
for i in x:
    if i%2 == 0:
        z.append(i)
        
print(*z)