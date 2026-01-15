n = int(input())
a = list(map(int, input().split()))

mini = float('inf')
for x in a:
    if x == 0:
        print(0)
        break
    mini = min(mini, abs(x))
else:
    print(mini)
