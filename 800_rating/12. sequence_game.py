testcases = int(input())
for _ in range ( testcases ) :
    n = int(input())
    b = list(map(int,input().split()))
    temp=[]
    temp.append(b[0])
    for i in range(1,n):
        if b[i-1] <= b[i]:
            temp.append(b[i])
        else:
            temp.append(b[i])
            temp.append(b[i])
    print(len(temp))
    print(*temp)