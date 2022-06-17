a = int(input())
x = list(map(int,input().split()))
k = int(input())
z = []

for i in x:
    if x.count(i) == k and i not in z:
        z.append(i)
        
if len(z) == 0:
    print(-1)
else:
    print(*z)