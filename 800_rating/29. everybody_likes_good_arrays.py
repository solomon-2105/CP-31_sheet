t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    i=0
    c=0
    while i<len(a)-1:
        if ( a[i]%2 == 0 and a[i+1]%2 == 0) or (a[i]%2 == 1 and a[i+1]%2 == 1):
            a[i] = a[i] * a[i+1]
            del a[i+1]
            c+=1
        else:
            i+=1
    print(c)