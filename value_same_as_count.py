a = int(input())
x = list(map(int,input().split()))
z = []

for i in x:
    if x.count(i) == i and i not in z:
        z.append(i)
        
print(len(z))