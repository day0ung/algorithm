T = int(input())

def anagram(a,b):

    if len(a) != len(b):
        return False

    if sorted(a) == sorted(b):
        return True
    else:
        return False


for _ in range(T):
    a, b = input().split()
    if anagram(a, b):
        print(a ,'&',b, 'are anagrams.')
    else:
        print(a, '&', b, 'are NOT anagrams.')

