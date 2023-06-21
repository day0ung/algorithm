N, M = map(int, input().split())
A = []
for _ in range(N):
    row = list(map(int, input().split()))
    A.append(row)

M, K = map(int, input().split())
B = []
for _ in range(M):
    row = list(map(int, input().split()))
    B.append(row)

# 행렬 A와 B의 곱셈
result = [[0] * K for _ in range(N)]
for i in range(N):
    for j in range(K):
        for k in range(M):
            result[i][j] += A[i][k] * B[k][j]

# 결과 출력
for row in result:
    print(' '.join(map(str, row)))