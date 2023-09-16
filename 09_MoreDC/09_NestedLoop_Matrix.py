def read_matrix():
    m = []

    nrows = int(input())

    for k in range(nrows):
        x = input().split()
        r = []

    for e in x:
        r.append( float(e) )
        m.append(r)
    return m

def mult_c(c, A):
    return [[c*A[i][j] for j in range(len(A[i])) ] for i in range(len(A))]

def mult(A, B):
    ans = []
    n,m = 

exec(input().strip())
