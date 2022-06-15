a = int(input())
x = list(map(int,input().split()))
sum = 0
for i in x:
    if i == 0 or i == 1:
        sum = sum + 1

if sum == len(x):
    print(True)
else:
    print(False)