testcases = int(input())
for _ in range ( testcases ) :
    m,n = map(int,input().split())
    a = input().strip()
    b = input().strip()
    found = False
    for i in range(6):
        if b in a:
            print(i)
            found = True
            break
        else:
            a+=a
    if not found:
        print(-1)