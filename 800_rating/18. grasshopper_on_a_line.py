testcases = int(input())
for _ in range(testcases):
    n , x = map(int , input().split())
    if n%x != 0:
        print(1)
        print(n)
    else:
        print(2)
        a , b = n-1 , 1
        print(a,b, sep=" ")