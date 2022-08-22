for i in range(int(input())):
    x = int(input())
    s = 1
    for i in range(x,1,-1):
        s = s*i
    print(s)