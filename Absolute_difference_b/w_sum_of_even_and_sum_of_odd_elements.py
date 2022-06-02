n = int(input())
x = list(map(int,input().split()))

s1 = s2 = 0

for i in x:
    if i%2==0:
        s1 = s1+i
    else:
        s2 = s2+i
        
print(abs(s1-s2))