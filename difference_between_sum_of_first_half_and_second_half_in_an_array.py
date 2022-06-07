n = int(input())
x = list(map(int,input().split()))
k = n//2
sum1 = sum2 = 0
for i in range(0,k):
    sum1 = sum1+x[i]
    
for i in range(k,n):
    sum2 = sum2+x[i]
    
print(abs(sum1-sum2))