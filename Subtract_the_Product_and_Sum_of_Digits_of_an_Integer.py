def ad(n):
    s = 0
    while n>0:
        r = n%10
        s =s+r
        n = n//10
    return s
def mul(n):
    p = 1
    while n>0:
        r = n%10
        p = p*r
        n = n//10
    return p

n = int(input())
print((mul(n))-(ad(n)))