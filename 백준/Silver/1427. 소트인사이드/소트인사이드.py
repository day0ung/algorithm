num = input()

arr = sorted(list(num), reverse=True)

for i in range(len(arr)):
  print(arr[i], end='')