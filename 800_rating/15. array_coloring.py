testcases = int(input())
for _ in range ( testcases ) :
    n = int(input())
    arr = list(map(int,input().split()))
    odd_count = sum(1 for x in arr if x % 2 == 1)
    if odd_count % 2 == 1:
        print("No")
    else:
        print("yes")