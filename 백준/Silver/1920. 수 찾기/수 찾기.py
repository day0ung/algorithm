N = int(input())
NA = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

NA.sort()

def binary_search(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == target:
            return True
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


for target in targets:
    if binary_search(NA, target):
        print(1)
    else:
        print(0)



