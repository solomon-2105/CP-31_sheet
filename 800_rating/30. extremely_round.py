def check(n):
    cz=cd=0
    while n:
        if n%10==0:
            cz+=1
        cd+=1
        n//=10
    return cz==cd-1

rounds=[]
for i in range(1,1_000_000):
    if check(i):
        rounds.append(i)

t=int(input())
for _ in range(t):
    x=int(input())
    ans=0
    for v in rounds:
        if v<=x: ans+=1
        else: break
    print(ans)