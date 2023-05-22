A = int(input())
B = str(input())

for i in reversed(B):  # 거꾸로 순서부터 해줘야함
    print(A * int(i))

print(A * int(B))