testcases = int(input())
for x in range(1,testcases+1):
    n = int(input())
    a = list(map(int,input().split()))
    b=[0]*n
    for i in range(n):
        b[i]=n+1-a[i]
    print(*b)