a = int(input())
x = list(map(int,input().split()))
m = min(x)
while True:
    s = 0
    for i in x:
        if i%m == 0:
            s = s+1
    if s == len(x):
        print(m)
        break
    m = m-1