def fibo(n):
    a = 0
    b = 1
    sum = 0
    for i in range(n-1):
        a = b
        b = sum
        sum = a+b
        print(sum,end=' ')
        
a = int(input())
print(0,end=' ')
fibo(a)