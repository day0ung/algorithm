A, B, V = map(int, input().split())

day = (V - B) // (A - B)  # 날짜 계산

if (V - B) % (A - B) != 0:  # 나머지가 있을 경우 하루를 더 추가
    day += 1

# 이코드는 시간이 초과됨..
# meter = 0
# day = 0
#
# while True:
#     day += 1
#     meter += A
#     if meter >= V:
#         break;
#     meter -= B

print(day)