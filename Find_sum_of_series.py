a = int(input())
k = []
for i in range(1,a+1):
    k.append(1/i)
sum = 0
for i in k:
    sum = sum+i
print("{:.2f}".format(sum))