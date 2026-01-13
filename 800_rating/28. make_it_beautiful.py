t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    maxi = max(a)
    if maxi == min(a):
        print("NO")
    else:
        a.remove(maxi)
        print("YES")
        print(maxi,end=" ")
        print(*a)
    print()