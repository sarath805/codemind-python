a = int(input())
x = list(map(int,input().split()))
sum = 0
for i in x:
    if i%2 == 0:
        sum = sum + 1
if sum == a:
    print(True)
else:
    print(False)