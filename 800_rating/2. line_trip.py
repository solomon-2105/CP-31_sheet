testcases = int(input())
for _ in range ( testcases ) :
    n , x = map (int , input(). split())
    a = list ( map ( int , input(). split()))
    a.insert(0 , 0)
    a.append(x)
    maxi = 0
    for i in range(len(a)-1) :
        if i == len(a)-2 :
            diff = (a[i+1] - a[i]) * 2
        else :
            diff = a[i+1] - a[i]
        maxi = max(maxi , diff) 
    print (maxi)