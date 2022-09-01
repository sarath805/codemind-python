def fib(n):
    a = 0
    b = 1
    s = 1
    z = [0,1,1]
    for i in range(n-3):
        a = b
        b = s
        s = a+b
        z.append(s)
    return z
a = int(input())
b = fib(a)
print(*b)