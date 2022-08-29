a = int(input())
p = []
for i in range(1,a+1):
    if a%i == 0:
        p.append((i,(a//i)))
        
c = []
for i in range(0,(len(p))//2):
    c.append(p[i])
def prime(a):
    s = 0
    for i in range(1,a+1):
        if a%i == 0:
            s =s+1
    if s == 2:
        return True
    else:
        return False
l = 0
o = []
for j in c:
    for k in j:
        if prime(k)==True:
            l = l+1
    if len(j) == l:
        o.append(j)
if len(o)==0:
    print(-1)
else:
    for i in o:
        print(*i)