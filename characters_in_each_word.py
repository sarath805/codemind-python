a = input()
s = a.split(" ")
t = []
for i in s:
    t.append(len(i))
    
print(*t)