def pali(n):
    s = str(n)
    a = s[::-1]
    if a == s:
        return True
    else:
        return False
for i in range(int(input())):
    k = int(input())
    print(pali(k))