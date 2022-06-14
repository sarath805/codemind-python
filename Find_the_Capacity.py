a,b,c = map(int,input().split())

k = 2*a*b*c*512

s = str(k//1024)

print(s+"KB")