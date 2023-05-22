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


#아래코드가 더 가독성이 좋음
#if M < 45:
#    H = (H - 1) % 24
#    M = (M - 45) % 60
#else:
#    M -= 45
