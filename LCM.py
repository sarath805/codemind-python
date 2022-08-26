a,b = map(int,input().split())
k = 1
while k>0:
    if k%a==0 and k%b==0:
        print(k)
        break
    k = k+1