a = int(input())
x = list(map(int,input().split()))
c,d = map(int,input().split())
sum = 0
for i in x:
    if i<c or i>d:
        sum = sum+i
print(sum)