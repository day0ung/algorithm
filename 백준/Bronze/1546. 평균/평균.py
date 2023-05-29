N = int(input())

list = list(map(int, input().split()))
list.sort(reverse=True)

avg = 0
for i in list:
    avg += i/list[0] * 100

print(avg/N)