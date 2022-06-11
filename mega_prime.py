def p(n):
    sum = 0
    for i in range(1,n+1):
        if n%i == 0:
            sum = sum +1
    if sum == 2:
        return True
    else:
        return False
        
a = int(input())
mp = True
if p(a)==True:
    while a>0:
        r = a%10
        if p(r)==False:
            mp = False
            break
        a = a//10
    if mp==True:
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")