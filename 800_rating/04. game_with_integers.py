testcases = int(input())
for _ in range(testcases):
    n = int(input())
    if n % 3 == 0:
        print("SECOND")
    else:
        print("FIRST")