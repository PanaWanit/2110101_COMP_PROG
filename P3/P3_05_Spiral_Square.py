def spiral_square(n): 
    l = [ [0 for i in range(n)] for j in range(n) ]
    d = [[0, -1, 0, 1], [-1, 0, 1, 0]]
    nd = 0
    now = n*n
    ni, nj = n-1, n-1
    while now!=0:
        l[ni][nj] = now
        now -= 1
        ii, jj = ni + d[0][nd],  nj + d[1][nd]
        if ii>n-1 or jj > n-1 or ii < 0 or jj < 0 or l[ii][jj]!=0:
            nd = (nd+1)%4
        ni, nj = ni + d[0][nd],  nj + d[1][nd]
    return l

def print_square(S):
    for i in range(len(S)):
        print(' '.join([(2*' '+str(e))[-3:] for e in S[i]]))

exec(input().strip())
