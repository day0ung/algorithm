H, M = map(int, input().split())
add = int(input())

H += add // 60
M += add % 60

H = H + 1 if M >= 60 else H 

if H % 24 == 0:
    H = 0
    print((H % 24), (M % 60))
else:
    print((H%24), (M % 60))