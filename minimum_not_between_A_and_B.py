a = int(input())
x = list(map(int,input().split()))
s, t = map(int,input().split())
z = []

for i in x:
    if i<s or i>t:
        z.append(i)
        
if len(z) == 0:
    print(-1)
else:
    print(min(z))