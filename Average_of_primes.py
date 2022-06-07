def prim(a):
    c = 1
    for i in range(1,a):
        if a%i==0:
            c = c+1
    if c == 2:
        return True
    else:
        return False

 
c = int(input())
b = list(map(int,input().split()))
sum = count = 0
for i in b:
    if prim(i)==True:
        sum = sum+i
        count = count+1

z = sum/count
print("{:.2f}".format(z))