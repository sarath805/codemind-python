m,n = map(int,input().split())
x = list(map(int,input().split()))
y = list(map(int,input().split()))

n1 = set(x)
n2 = set(y)

a = n1.symmetric_difference(n2)
print(len(a))
