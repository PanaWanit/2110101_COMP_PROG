def reverse(d):
    a = {}
    for i,j in d.items():
        a[j] = i
    return a
        
def keys(d, v):
    return [x for x, k in d if k==v]

exec(input().strip())
