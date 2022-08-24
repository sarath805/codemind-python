def num(n):
    s = []
    while n>0:
        r = n%10
        s.append(r)
        n = n//10
    return s
def fact(a):
    f = 1
    for i in range(1,a+1):
        f = f*i
    return f
a = int(input())
b = num(a)
sum = 0
for i in b:
    sum = sum+fact(i)
if sum == a:
    print("The number",a,"is a strong number")
else:
    print("The number",a,"is not a strong number")