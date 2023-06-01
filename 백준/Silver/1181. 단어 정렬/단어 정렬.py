T = int(input())

words = set()
for _ in range(T):
    words.add(input())

sorted_words = sorted(words, key=lambda x: (len(x), x))
# lambda x: (len(x), x)는 길이를 우선으로 비교하고, 길이가 같은 경우에는 문자열 자체인 x를 비교

for i in sorted_words:
    print(i)