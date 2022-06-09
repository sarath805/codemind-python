a = input()
c = a[0].lower() + a[1:]
x = list(c)
x.reverse()
y = list(c)

if x==y:
    print(True)
else:
    print(False)