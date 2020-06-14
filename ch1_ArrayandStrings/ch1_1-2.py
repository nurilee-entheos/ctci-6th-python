# Answer A

def checkPermutation(str1, str2):
    if len(str1) != len(str2):
        return False
    if sorted(list(str1)) != sorted(list(str2)):
        return False
    return True
    

print(checkPermutation("apple","mango"))

print(checkPermutation("key","boil"))

print(checkPermutation("apple","elppa"))

print(checkPermutation("aabbb","bbaaa"))

# Answer B

from collections import Counter

def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    counter = Counter()
    counter.update(str1)
    print(counter)

    for c in str2:
        if counter[c] == 0:
            return False
        counter[c] -= 1
        print(c, counter)
    return True

print(check_permutation("apple","mango"))

print(check_permutation("key","boil"))

print(check_permutation("apple","elppa"))

print(check_permutation("aplee","elppa"))

print(check_permutation("aabbb","bbaaa"))



