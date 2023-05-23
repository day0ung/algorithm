N, K = map(int, input().split())

X = map(int, input().split())

score = []
for i in X:
    score.append(i)

score.sort()

print(score[N-K])