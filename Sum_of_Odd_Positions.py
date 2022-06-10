a = int(input())
x = list(map(int,input().split()))
sum = 0
for i in range(a):
    if i%2 != 0:
        sum = x[i]+sum
        
print(sum)