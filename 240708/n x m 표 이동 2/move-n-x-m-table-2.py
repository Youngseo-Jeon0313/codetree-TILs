N, M = map(int,input().split())
Board = []
for _ in range(N):
    Board.append(list(map(int,input().split())))

DP_UP = [[-float('inf') for _ in range(M)] for _ in range(N)]
DP_DOWN = [[-float('inf') for _ in range(M)] for _ in range(N)]

# DP_UP[i][j]=max(DP[i][j], DP[i+1][j]+Board[i][j], DP[i][j-1]+Board[i][j])
for i in range(N-1, -1, -1): # 밑바닥부터
    for j in range(M): 
        if i == N-1 and j == 0 :
            DP_UP[i][j] = Board[i][j]
        else:
            if i+1 != N:
                DP_UP[i][j] = max(DP_UP[i][j], DP_UP[i+1][j]+Board[i][j])
            if j-1 != -1:
                DP_UP[i][j] = max(DP_UP[i][j], DP_UP[i][j-1]+Board[i][j])

# DP_DOWN[i][j]=max(DP[i][j], DP[i-1][j]+Board[i][j], DP[i][j+1]+Board[i][j])
for i in range(N-1, -1, -1): # 밑바닥부터
    for j in range(M-1, -1, -1):
        if i == N-1 and j == M-1:
            DP_DOWN[i][j] = Board[i][j]
        else:
            if i+1!= N:
                DP_DOWN[i][j] = max(DP_DOWN[i][j], DP_DOWN[i+1][j]+Board[i][j])
            if j+1 != M:
                DP_DOWN[i][j] = max(DP_DOWN[i][j], DP_DOWN[i][j+1]+Board[i][j])

# for i in DP_UP:
#     print(*i)
# for j in DP_DOWN:
#     print(*j)
    

answer = -float('inf')
for i in range(N):
    for j in range(M):
        answer = max(answer, DP_UP[i][j]+DP_DOWN[i][j])

print(answer)