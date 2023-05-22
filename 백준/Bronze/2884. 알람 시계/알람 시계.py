H, M = input().split()

H = int(H)
M = int(M)

if(M < 45):
    H -= 1
    M = (M - 45) + 60
    if(H < 0):
        H = 24 + H
else:
    M -= 45

print(H, M)