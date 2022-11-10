def first_fit(l, e):
    choose=0
    for i in range(len(l)):
        s = sum(l[i])
        if e + s <= 100:
            l[i].append(e)
            choose=1
            break
        if choose:
            break
    if choose==0:
        l.append([e])
        
def best_fit(l, e):
    choose=0
    best_idx=0
    mn=100
    for i in range(len(l)):
        s = sum(l[i])
        if e + s <= 100:
            choose=1
            if 100-e-s<mn:
                mn = 100-e-s
                best_idx = i
    if choose==0:
        l.append([e])
    else:
        l[best_idx].append(e)

def partition_FF(D):
    l = []
    for i in D:
        first_fit(l, i)
    return l

def partition_BF(D):
    l = []
    for i in D:
        best_fit(l, i)
    return l

exec(input().strip())
