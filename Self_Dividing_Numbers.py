a = int(input())
b = int(input())
k = a
for i in range(a,b+1):
    j = i
    while i!=0:
        r = i%10
        i = i//10
        if r==0:
            break
        if j%r!=0:
            break
    else:
        print(j, end = " ")