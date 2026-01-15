testcases = int(input())
for _ in range ( testcases ) :
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    if k in a:
        print("YES")
    else:
        print("NO")