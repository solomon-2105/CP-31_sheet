testcases = int(input())
for _ in range ( testcases ) :
    n = int(input())
    a = list(map(int, input().split()))
    s = 0
    for i in a:
        s^=i
    if n%2 == 1:
        print(s)
    else:
        print(0 if s==0 else -1) 