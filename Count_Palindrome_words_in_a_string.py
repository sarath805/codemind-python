a = input()
s = a.split(" ")
z = []
for i in s:
    z.append(i[0].lower()+i[1:])
 
sum = 0  
for j in z:
    k = list(j)
    k.reverse()
    l = list(j)
    
    if k == l:
        sum = sum+1
        
print(sum)
    