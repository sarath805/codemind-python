a = int(input())
n = list(map(int,input().split()))
b = max(n)
while True:
    s = 0
    for i in n:
        if b%i == 0:
            s = s+1
    if s == len(n):
        print(b)
        break
    b = b+1