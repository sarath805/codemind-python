a = int(input())
b = list(map(int,input().split()))
av = sum(b)//len(b)
s = [i for i in b if i>=av]
print(len(s))