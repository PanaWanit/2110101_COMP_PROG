a = float(input())
t=int(a)
l,r=0,0

while t!=0:
    t//=10
    r+=1

def limit(a, b):
    return abs(a-b) <= 1e-10*max(abs(a), abs(b))

m = (l+r)/2

while not limit(10**m, a):
    if 10**m > a:
        r = m
    else:
        l = m
    m = (l+r)/2
print(round(m, 6))
