a,b = map(int,input().split())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
z = []
for i in x:
    if i in y and i not in z:
        z.append(i)
        
print(*z)