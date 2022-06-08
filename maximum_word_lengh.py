a = input()
s = a.split(" ")
l = []

for i in s:
    l.append(len(i))
    
print(max(l))