testcases = int(input())
for x in range(1,testcases+1):
    n = int(input())
    a = list(map(int,input().split()))
    c , m = 0, 0
    for i in a:
        if i==0:
            c+=1
            m=max(m, c)
        else:
            c=0
    print(m)