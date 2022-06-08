a = input()
l = a.split(" ")
k = m = n = []

for i in range(len(l)):
    if i%2==0:
        k.append(l[i][::-1])
    else:
        m.append(l[i])
    n = k+m
for i in m:
    print(i,end=' ')