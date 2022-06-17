a = int(input())
x = list(map(int,input().split()))
z = []

for i in x:
    if x.count(i) == i and i not in z:
        z.append(i)
        
if len(z) == 0:
    print(-1)
else:
    print(min(z),max(z),end = " ")