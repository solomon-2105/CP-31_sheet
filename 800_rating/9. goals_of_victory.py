testcases = int(input())
for _ in range ( testcases ) :
    n = int(input())
    a = list(map(int,input().split()))
    print(-1*sum(a))