a = int(input())
x = list(map(int,input().split()))
avg = sum(x)//len(x)

if avg in x:
    print(True)
else:
    print(False)