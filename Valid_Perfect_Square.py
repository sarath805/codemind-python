def per(n):
    x = n**0.5
    if x==int(x):
        return True
    else:
        return False
for i in range(int(input())):
    p = int(input())
    print(per(p))