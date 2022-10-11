for i in range(int(input())):
    a = int(input())
    #before prime
    k = a
    p = 0
    while k>0:
        s = 0
        for i in range(1,k+1):
            if k%i == 0:
                s = s+1
        if s == 2:
            p = p+k
            break
        k = k-1
    #after prime
    q = 0
    m = a
    while k>0:
        s = 0
        for j in range(1,m+1):
            if m%j == 0:
                s = s+1
        if s == 2:
            q = m
            break
        m = m+1
    #near prime
    if abs(a-p) <= abs(a-q):
        print(p)
    else:
        print(q)