a = int(input())
x = 0
l = []
p = 1
while x<a:
    x = (2**p)
    l.append(x)
    p = p+1
m = l[len(l)-1]
n = l[len(l)-2]
print(min(abs(m-a),abs(n-a)))