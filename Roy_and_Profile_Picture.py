l = int(input())
n = int(input())
for i in range(n):
    w,h = map(int,input().split())
    if w>=l and h>=l:
        if w == h:
            print("ACCEPTED")
        else:
            print("CROP IT")
    elif w<l or h<l:
        print("UPLOAD ANOTHER")