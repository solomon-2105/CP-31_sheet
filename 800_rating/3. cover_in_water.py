testcases = int(input())
for _ in range ( testcases ) :
    n = int(input())
    s = input().strip()
    count , found = 0 , False
    for i in s:
        if i == '.' :
            count += 1
            if count == 3 :
                print("2")
                found = True
                break
        else :
            count = 0
    if not found :
        a = s.count('.')
        print( a )