a = int(input())
x = list(map(int,input().split()))
e, f = map(int,input().split())
z = []

for i in x:
    if i>=e and i<=f:
        z.append(i)
        
if len(z) == 0:
    print(-1)
else:
    print(min(z))