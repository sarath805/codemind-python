a = int(input())
b = list(map(int,input().split()))
c = set(b)
sum = 0
for i in c:
    if i%2 == 0:
        sum = sum+1
print(sum)