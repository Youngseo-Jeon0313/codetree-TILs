N = int(input())
List = list(map(int,input().split()))

min_ans = float('inf')

for i in range(N): #지정된 장소
    temp_ans = 0
    for j in range(N):
        temp_ans += abs(j-i)*List[j]
    min_ans = min(min_ans, temp_ans)

print(min_ans)