a = int(input())
b = list(map(int,input().split()))
c = int(input())
sum = 0
for i in range(0,c):
    sum = sum+b[i]
    
print(sum)