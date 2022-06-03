a = int(input())
x = list(map(int,input().split()))
x.reverse()

for i in x:
    if i%2 != 0:
        print(i)
        break