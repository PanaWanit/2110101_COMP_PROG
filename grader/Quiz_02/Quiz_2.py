def sum_char(c, word):
    s = 0
    for i in word:
        if c==i:
            s += 1
    return s

def match(word, pattern, include, exclude):
    if len(word) != len(pattern):
        return False
    l = ""
    for i in range(len(word)):
        if pattern[i] == '?':
            if word[i] in exclude:
                return False
            l += word[i]
            continue
        if word[i] != pattern[i]:
            return False

    for i in include:
        if sum_char(i, include) > sum_char(i, l):
            return False

    return True


exec(input())
