testcases = int(input())
for _ in range ( testcases ) :
    a,b,c = map(int,input().split())
    if a==b:
        if c%2==1:
            print("First")
        else:
            print("Second")
    else:
        if a > b:
            print("First")
        else:
            print("Second")