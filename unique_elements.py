def u(n):
    
    z = []
    for i in n:
        if i not in z:
            z.append(i)
    print(*z)

a = int(input())
x = list(map(int,input().split()))
u(x)