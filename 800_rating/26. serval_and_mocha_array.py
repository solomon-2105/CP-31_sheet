import math
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int,input().split()))
        found = False
        for i in range(n):
            for j in range(i+1,n):
                gcd = math.gcd(a[i],a[j])
                if gcd <= 2:
                    print("YES")
                    found = True
                    break
            if found:
                break
        if not found:
            print("NO")