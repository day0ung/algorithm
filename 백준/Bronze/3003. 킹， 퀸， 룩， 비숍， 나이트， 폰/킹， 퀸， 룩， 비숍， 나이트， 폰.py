chess = [1,1,2,2,2,8]

T = list(map(int, input().split(" ")))

for i, v in enumerate(T):
   print(chess[i] - v, end=' ')

# 리스트 컴프리헨션을 사용하여 결과를 한 줄로 출력가능
# ([chess[i] - v for i, v in enumerate(T)])