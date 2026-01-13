t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = 0
    for i in a:
        if i == 2:
            b += 1
    if b == 0:
        print(1)
        continue
    if b%2 == 1 : 
        print(-1)
        continue
    c = 0
    for i in range(n):
        if a[i] == 2:
            c+=1
            if c == b//2:
                print(i+1)
                break