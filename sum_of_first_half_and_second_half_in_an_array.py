a = int(input())
x = list(map(int,input().split()))
k = int(a/2)
sum1 = sum2 = 0
for i in range(0,k):
    sum1 = sum1+x[i]

print(sum1)
print(abs(sum(x)-sum1))