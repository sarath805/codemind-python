a = input()
e = []
o = []
for i in list(a):
    if int(i)%2 == 0:
        e.append(i)
    else:
        o.append(i)
        
if len(e) == len(a):
    print("Even")
elif len(o) == len(a):
    print("Odd")
else:
    print("Mixed")