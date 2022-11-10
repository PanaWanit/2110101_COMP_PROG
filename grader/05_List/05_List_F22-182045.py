def index_of(grades, ID):
    for i in range(len(grades)):
        if grades[i][0] == ID:
            return i
    return -1

def up(x):
    if x=='A':
        return 'A'
    if x=='B+':
        return 'A'
    if x=='B':
        return 'B+'
    if x=='C+':
        return 'B'
    if x=='C':
        return 'C+'
    if x=='D+':
        return 'C'
    if x=='D':
        return 'D+'
    if x=='F':
        return 'D'

def upgrade(g, IDs):
    g[:] = sorted(g)
    for l in IDs:
        for x in g:
            if x[0]==l:
                x[1] = up(x[1])

exec(input())
exec(input())
exec(input())
