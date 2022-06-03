a = int(input())
x = list(map(int,input().split()))
avg = sum(x)//len(x)

s = [i for i in x if i<=avg]
print(len(s))