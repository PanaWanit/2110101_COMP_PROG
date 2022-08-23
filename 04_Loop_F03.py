def grade_mcq(a, b):

    if len(a) != len(b):
        return -1
    c=0
    for i in range(len(a)):
        if a[i] == b[i]:
            c+=1
    return c
exec(input())
