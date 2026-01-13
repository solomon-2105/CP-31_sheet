testcases = int(input())
for _ in range ( testcases ) :
    sx,sy,dx,dy = map(int,input().split())
    if dy<sy:
        print(-1)
    else:
        cost=dy-sy
        sx+=cost
        if sx<dx:
            print(-1)
            continue
        cost+=sx-dx
        print(cost)