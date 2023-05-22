total = int(input())
product = int(input())

result = 0
for i in range(product):
    price,count = map(int, input().split())
    result += price * count

answer = 'Yes' if result == total else 'No'

print(answer)