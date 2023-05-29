T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    k0 = [i for i in range(1, n + 1)]  # 0층의 1호부터 n호까지의 리스트

    for j in range(k):  # 층수만큼 반복
        for x in range(1, n): # 호수만큼
         k0[x] += k0[x - 1]  # 1부터 시작하는 인덱스 범위를 고려하여 [x-1]

    print(k0[-1])  # 리스트의 마지막을 출력