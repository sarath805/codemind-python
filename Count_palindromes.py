def rev(n):
    sum = 0
    while n>0:
        r = n%10
        sum = sum*10+r
        n = n//10
    return sum
    
def palin(c):
    if c == rev(c):
        return True
    else:
        return False
        
a = int(input())
x = list(map(int,input().split()))
c1 = 0
for i in x:
    if palin(i)==True:
        c1 = c1+1
print(c1)