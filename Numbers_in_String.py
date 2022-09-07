x = input()
a = list(x)
p = []
for i in a:
    if i in "1234567890":
        p.append(i)
s = 0
for i in p:
    s =s+int(i)
print(s)