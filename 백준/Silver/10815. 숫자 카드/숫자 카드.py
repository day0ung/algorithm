import sys

n = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))
card.sort()
m = int(sys.stdin.readline())
targets = list(map(int, sys.stdin.readline().split()))

def binary(array, target):
    left = 0
    right = len(array) -1
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
    if binary(card, target):
        print(1, end=' ')
    else:
        print(0, end=' ')
