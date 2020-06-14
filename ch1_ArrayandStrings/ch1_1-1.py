# Answer A
def isUniqueA(s):
    return len(set(s)) == len(s)

print(isUniqueA("strawberry"))

# Answer B

def isUniqueB(s):
    uchars = set()
    for c in s:
        if c in uchars:
            return False
        uchars.add(c)
    return True

print(isUniqueB("strawberry"))

# Answer C

def isUniqueC(str_input):
    str_list = list(str_input)
    check_list = []
    for s in str_list:
        if s not in check_list:
            check_list.append(s)
        else:
            return False
    return True

print(isUniqueC("strawberry"))

# Answer D - Text Book First Answer

def isUniqueD(string):
    # Assuming character set is ASCII (128 characters)
    if len(string) > 128:
        return False

    char_set = [False for _ in range(128)]
    for char in string:
        val = ord(char)
        if char_set[val]:
            # Char already found in string
            return False
        char_set[val] = True

    return True

print(isUniqueD("strawberry"))

# Answer E - Text Book Second Answer

def isUniqueE(string):
  checker = 0
  for c in string:
    val = ord(c) - ord('a')
    if (checker & (1 << val) > 0):
      return False
    checker |= (1 << val)
  return True

print(isUniqueE("strawberry"))
