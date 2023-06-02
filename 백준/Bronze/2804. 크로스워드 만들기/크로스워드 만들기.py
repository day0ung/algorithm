A, B = input().split()

# 공유글자 찾기
for i in range(len(A)):
    if A[i] in B:
        share = A[i]
        A_idx = i
        break
        
# B에서의 공유 글자 위치 찾기
for i in range(len(B)):
    if B[i] == share:
        B_idx = i
        break

result = ['.'] * len(A)
for i in range(len(B)):
    result[A_idx] = B[i]
    if i == B_idx:
        print(A)
    else:
        print("".join(map(str, result)))