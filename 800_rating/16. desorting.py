testcases = int(input())
for _ in range ( testcases ) :
    n = int(input())
    a = list(map(int,input().split()))
    for i in range(1,n):
        if a[i] < a[i-1]:
            print(0)
            break
    else:
        min = float('inf')
        dif = 0
        b,c = -1,-1
        for i in range(1,n):
            dif = a[i]-a[i-1]
            if dif < min:
                min = dif
                b , c = i, i-1
        print((min//2)+1)