def non_prime(n):
    s = 0
    for i in range(1,n+1):
        if n%i == 0:
            s = s+1
    if s>2:
        return True
    else:
        return False
        
a = int(input())
z = []
for i in range(1,a+1):
    if a%i == 0:
        z.append(i)
sum = 1
for j in z:
    if non_prime(j) == True:
        sum =sum+1
        
print(sum)