testcases = int(input())
for _ in range ( testcases ) :
    n = int(input())
    a = list(map(int, input().split()))
    hashmap = {}
    for i in a :
        hashmap[i] = hashmap.get(i, 0) + 1
    if len(hashmap) >= 3 :
        print("NO")
    else :
        vals = list(hashmap.values())
        if len(vals) == 1:
            print("YES")
        else:
            diff = abs(vals[0] - vals[1])
            print("YES" if diff <= 1 else "NO")