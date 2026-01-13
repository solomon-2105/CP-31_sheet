testcases = int(input())
for _ in range(testcases):
    mat = []
    score = 0
    for _ in range(10):
        mat.append(list(input().strip()))
    for i in range(10):
        for j in range(10):
            if mat[i][j] == 'X':
                if i==0 or i==9 or j==0 or j==9:
                    score += 1
                elif i==1 or i==8 or j==1 or j==8:
                    score += 2
                elif i==2 or i==7 or j==2 or j==7:
                    score += 3
                elif i==3 or i==6 or j==3 or j==6:
                    score += 4
                else:
                    score += 5
                
    print(score)