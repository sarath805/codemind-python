def add(n):
    sum = 0
    while n>0:
        r = n%10
        sum = sum+r
        n = n//10
    return sum
    
a = int(input())
x = list(map(int,input().split()))
z = []

for i in x:
    z.append(add(i))
    
print(sum(z))