def choose(s1, s2):
    f1,f2 = False, False

    if s1[2] != 'A' or s1[3] > 'C' or s1[4] > 'C':
        f1 = True
    if s2[2] != 'A' or s2[3] > 'C' or s2[4] > 'C':
        f2 = True

    if f1 == True and f2 == True:
        return []
    elif f1 == True:
        return [s2[0]]
    elif f2 == True:
        return [s1[0]]

    if s1[1] > s2[1]:
        return [s1[0]]
    if s2[1] > s1[1]:
        return [s2[0]]

    if s1[3] < s2[3]:
        return [s1[0]]
    if s2[3] < s1[3]:
        return [s2[0]]

    if s1[4] < s2[4]:
        return [s1[0]]
    if s2[4] < s1[4]:
        return [s2[0]]

    return [s1[0], s2[0]]

exec(input())
