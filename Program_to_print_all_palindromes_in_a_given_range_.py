def pali(n):
    a = str(n)
    b = a[::-1]
    if a == b:
        return True
    else:
        return False
a = int(input())
b = int(input())
for i in range(a,b+1):
    if pali(i) == True:
        print(i,end = ' ')