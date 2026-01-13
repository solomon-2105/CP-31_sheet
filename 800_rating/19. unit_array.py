testcases = int(input())
for x in range(1,testcases+1):
    n = int(input())
    a = list(map(int,input().split()))
    neg = 0
    for i in a:
        if i == -1: neg+=1
    pos = n - neg
    c=0
    while neg > pos or neg%2==1:
        neg-=1
        pos+=1
        c+=1
    print(c)