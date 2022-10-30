a,b = map(int,input().split())
x = list(map(int,input().split()))
c = 0
for i in range(len(x)):#1
    s = 0
    for j in range(i,len(x)):#1,3
        s = s+x[j]
        if s == b:
            c = c+1
print(c)