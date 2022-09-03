a = input()
b = a[::-1]
c = list(b)
s = ''
if c[0] == "0":
    c.pop(0)
if c[len(c)-1] == "-":
    c[0] == "-"
    c.pop(len(c)-1)
for i in c:
    s = s+i
if "-" in a:
    print('-'+s)
else:
    print(int(s))