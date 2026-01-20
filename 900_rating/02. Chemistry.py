testcases = int(input())
for _ in range(testcases):
    n , k = map(int,input().split())
    s = input().strip()
    a ={}
    for i in s:
        a[i] = a.get(i,0)+1
    b = list(a.values())
    c = 0
    for i in b:
        if i % 2 == 1:
            c += 1
    if c > (k + 1):
        print("NO")
    else:
        print("YES")
    print()
    print()