def rev(n):
    sum = 0
    while n>0:
        r = n%10
        sum = sum*10+r
        n = n//10
    return sum

a = int(input())
x = list(map(int,input().split()))
l = []
for i in x:
    l.append(rev(i))

print(*l)