a,b,c = map(int,input().split())
S = (a+b+c)/2
s = round(S,2)
a = s*(s-a)*(s-b)*(s-c)
x = a**(1/2)
print("{:.2f}".format(x))