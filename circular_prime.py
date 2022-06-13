def prime(n):
    s = 0
    for i in range(1, n + 1):
        if n%i == 0:
            s = s + 1
    if s == 2:
        return True
    else:
        return False
        
def rev(n):
    sum = 0
    while n>0:
        r = n%10
        sum =sum*10+r
        n = n//10
    return sum
    
a = int(input())
b = rev(a)
if prime(a) == True and prime(b) == True:
    print("circular prime")
elif prime(a) == True and prime(b) != True:
    print("prime but not a circular prime")
else:
    print("not prime")