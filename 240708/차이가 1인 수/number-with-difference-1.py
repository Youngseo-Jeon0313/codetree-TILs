N = int(input())

DP = [[0 for _ in range(101)] for _ in range(10)] #DP[~로 끝나는 애들][자리수]

for i in range(10):
    if i==0: continue
    DP[i][1]=1
if N ==1: print(0); exit()
for j in range(2,101):
    for i in range(10):
        if i==0:
            DP[i][j]+=DP[i+1][j-1]
        elif i==9:
            DP[i][j]+=DP[i-1][j-1]
        else:
            DP[i][j]+=DP[i+1][j-1]
            DP[i][j]+=DP[i-1][j-1]
answer = 0
for i in range(10):
    answer+=DP[i][N]

print(answer%(10**9+7))