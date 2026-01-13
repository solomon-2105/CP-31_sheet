testcases = int(input())
for _ in range ( testcases ) :
    n = int(input())
    a = list(map(int,input().split()))
    if len(set(a)) == 1:
        print(-1)
        continue
    marked = []
    unmarked = []
    maxi = max(a)
    for i in a:
        if i == maxi:
            marked.append(i)
        else:
            unmarked.append(i)
    print(len(unmarked), len(marked) , sep=' ')
    print(*unmarked)
    print(*marked)