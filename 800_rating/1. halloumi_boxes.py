def check(a):
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            return False
    return True
testcases = int(input())
for _ in range ( testcases ) :
    n , k= map (int , input(). split())
    a = list ( map ( int , input(). split()))
    b = check(a)
    if b :
        print ( "YES" )
    else :
        if k == 1 :
            print ( "NO" )
        else :
            print ( "YES" )