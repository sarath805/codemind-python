a,b = map(int,input().split())
x = list(map(int,input().split()))
y = list(map(int,input().split()))

s1 = set(x)
s2 = set(y)

ass = s1.symmetric_difference(s2)
print(len(ass))