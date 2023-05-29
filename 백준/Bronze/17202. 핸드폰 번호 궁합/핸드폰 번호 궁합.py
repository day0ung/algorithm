a_list = list(map(int, str(input())))
b_list = list(map(int, str(input())))

c = list(zip(a_list, b_list))
c = [elem for pair in c for elem in pair] # c의 각 튜플 (x, y)에서 x와 y를 순서대로 추출하여 하나의 리스트로 만듬

while len(c) > 2:
    temp = []
    for i in range(len(c) -1):
        sum = (c[i] + c[i +1]) % 10
        temp.append(sum)

    c = temp

print(''.join(map(str, c)))




