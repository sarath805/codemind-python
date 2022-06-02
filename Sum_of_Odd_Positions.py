n = int(input())
l = list(map(int,input().split()))
sum = 0
for i in range(n):
    if i%2 !=0:
        sum = sum+l[i]
print(sum)