n = int(input())

origin = n
cnt = 0

while True:

    if n < 10:
        n = '0'+ str(n)

    left = int(n) //10
    right = int(n) % 10
    sum = left + right

    n = int(str(right) + str(sum%10))
    cnt += 1
    if n == origin:
        break

print(cnt)