def letter_point(c):
    if c in "AEILNORSTU":
        return 1
    if c in "DG":
        return 2
    if c in "BCMP":
        return 3
    if c in "FHVWY":
        return 4
    if c in "K":
        return 5
    if c in "JX":
        return 8
    if c in "QZ":
        return 10

def word_point(w):
    s = 0
    for i in w:
        s += letter_point(i)
    return s

ans = []
for i in input().split():
    ans.append([-word_point(i), i])

ans.sort()

for b,a in ans:
    print(a, -b)
