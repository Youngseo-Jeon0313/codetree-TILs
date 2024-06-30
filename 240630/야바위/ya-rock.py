N = int(input())
List = []
for _ in range(N):
    a,b,c = map(int,input().split())
    List.append((a,b,c))

# 1 0 0 으로 시작
cups1 = [1, 0, 0]
ans_1 = 0
for i in range(N):
    a, b, c = List[i]
    a-=1; b-=1; c-=1;
    cups1[a],cups1[b]=cups1[b], cups1[a]
    ans_1 += cups1[c]

# 0 1 0 으로 시작
cups2 = [0, 1, 0]
ans_2 = 0
for i in range(N):
    a, b, c = List[i]
    a-=1; b-=1; c-=1;
    cups2[a],cups2[b]=cups2[b], cups2[a]
    ans_2 += cups2[c]

# 0 0 1 으로 시작
cups_3 = [0,0,1]
ans_3 = 0
for i in range(N):
    a, b, c = List[i]
    a-=1; b-=1; c-=1;
    cups_3[a],cups_3[b]=cups_3[b], cups_3[a]
    ans_3 += cups_3[c]
#print(ans_1, ans_2, ans_3)
print(max(ans_1, ans_2, ans_3))