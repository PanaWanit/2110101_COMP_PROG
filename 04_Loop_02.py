def limit(a, b):
    return abs(a-b) <= 1e-10*max(abs(a), abs(b))
a = float(input())

l,r = 0, a
m = (l+r)/2

while l < r :
    m = (l+r)/2
    if 10**m > a:
        r=m
    else:
        l=m
    if limit(a, 10**m):
        print(round(m, 6))
        quit()
"""
while not limit(10**m, a):
    if 10**m > a:
        r = m
    else:
        l = m
    m = (l+r)/2
print(round(m, 6))
"""
