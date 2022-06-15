a = int(input())
x = list(map(int,input().split()))

sum = 0
for i in x:
    sum = sum*10+i
    
a = str(sum)
print(int(a,2))