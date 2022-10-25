fa, fb = input().split()

def read_next(f):
    t = f.readline()
    if len(t) == 0:
        return "", ""
    x = t.strip().split()
    if len(x) == 2:
        return x[0], x[1]


fa = open(fa, 'r')
fb = open(fb, 'r')

ta, sa = read_next(fa)
tb, sb = read_next(fb)

while ta!="" or tb!="":
    if ta=="":
        print(tb, sb)
        tb,sb = read_next(fb)
        continue
    elif tb=="":
        print(ta, sa)
        ta,sa = read_next(fa)
        continue
    if ta[-2:] < tb[-2:]:
        print(ta, sa)
        ta,sa = read_next(fa)
    elif ta[-2:] > tb[-2:]:
        print(tb, sb)
        tb,sb = read_next(fb)
    else:
        if ta < tb:
            print(ta, sa)
            ta,sa = read_next(fa)
        else:
            print(tb, sb)
            tb, sb = read_next(fb)
