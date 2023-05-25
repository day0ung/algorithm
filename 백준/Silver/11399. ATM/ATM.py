n = int(input())  # 첫째줄 입력

peoples = list(map(int, input().split()))

peoples.sort()  # 작은 순서대로 정렬
answer = 0  # 정답 변수를 0으로 선언

for i in range(1, n+1):
    answer += sum(peoples[0:i])  # 리스트의 0번째 수부터 i번째 수까지를 더함
print(answer)