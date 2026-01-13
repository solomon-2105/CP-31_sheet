t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    i,j = 0,n-1
    while i<=j and s[i]!=s[j]:
        n-=2
        i+=1
        j-=1
    print(n)
