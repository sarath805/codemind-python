n, k = map(int,input().split())
x = list(map(int,input().split()))
z =[]

for i in x:
    if i%k != 0:
        z.append(i)
        
print(len(z))