a = int(input())
x = list(map(int,input().split()))
s, t = map(int,input().split())

sum = 0
for i in x:
    if i>=s and i<=t:
        sum = sum+i
        
print(sum)