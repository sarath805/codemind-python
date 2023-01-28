def noop(a,l):
    b = l
    s = set(l)
    p = 0
    for i in s:
        o = l.count(i)
        k = o//2
        p = p+k
    return p
a = int(input())
l = list(map(int,input().split()))
print(noop(a,l))