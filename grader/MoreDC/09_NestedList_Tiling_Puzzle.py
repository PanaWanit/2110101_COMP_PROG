def row_number(t, e):
    for i,row in enumerate(t):
        if e in row:
            return i
    return 0

def flatten(t):
    return [i for j in t for i in j if i!=0]

def inversions(a):
    c=0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] > a[j]:
                c+=1
    return c

def solvable(a):
    if len(a) % 2 == 1:
        if(inversions(flatten(a))%2==0):
            return True
        return False
    else:
        if inversions(flatten(a))%2==0:
            if row_number(a, 0)%2==1:
                return True
            return False
        else:
            if row_number(a, 0)%2==0:
                return True
            return False



exec(input().strip())
