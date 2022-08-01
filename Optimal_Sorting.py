t = int(input())
for i in range(t):
    n = int(input())
    x = list(map(int,input().strip().split()))
    a = x[len(x)-1]
    if a == max(x):
        print(0)
    else:
        print(max(x)-min(x))