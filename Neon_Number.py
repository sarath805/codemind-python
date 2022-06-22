def add(n):
    sum = 0
    while n>0:
        r = n%10
        sum = sum +r
        n=n//10
    return sum

a = int(input())
b = a**2

if a == add(b):
    print("Neon Number")
else:
    print ("Not Neon Number")