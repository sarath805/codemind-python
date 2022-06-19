a = int(input())
x = list(map(str,input().split()))
z = []

for i in x:
    z.append(len(i))
    
m = max(z)

for j in x:
    if len(j)==m:
        print(j,end = ' ')