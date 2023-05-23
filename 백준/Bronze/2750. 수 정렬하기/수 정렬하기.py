N = int(input())

numbers = []

for i in range(N):
    numbers.append(int(input()))

for j in sorted(numbers):
    print(j)