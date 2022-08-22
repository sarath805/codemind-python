i,t,k = map(int,input().split())
s = 0
for i in range(i,t+1):
    if i%k == 0:
        s = s+1
print(s)