a,b = map(int,input().split())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
z = []
for i in x:
    if i not in y:
        z.append(i)
for j in y:
    if j not in x:
        z.append(j)
        
print(*z)