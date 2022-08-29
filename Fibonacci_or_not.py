x = int(input())
a = 0
b = 1
sum = a+b
p = []
for i in range(x):
    a = b
    b = sum
    sum = a+b
    p.append(sum)
if x in p:
    print(True)
else:
    print(False)