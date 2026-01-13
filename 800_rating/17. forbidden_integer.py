testcases = int(input())
for _ in range ( testcases ) :
    n,k,x = map(int,input().split())
    if x != 1:
        print("YES")
        print(n)
        for _ in range(n):
            print(1,end=' ')
        print()
    else:
        if k == 1:
            print("NO")
            continue
        else:
            if n%2 == 0:
                print("YES")
                print(n//2)
                for _ in range(n//2):
                    print(2,end=' ')
                print()
            else:
                if k == 2:
                    print("NO")
                    continue
                print("YES")
                q = n//2
                print(q)
                for i in range(q-1):
                    print(2,end=' ')
                print(3,end=' ')
                print()