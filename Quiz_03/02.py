n,m,k = [int(_) for _ in input().split()]
f = dict()

for i in range(n):
    name, faculty = input().split()
    f[name] = faculty

d = dict()
for i in range(m):
    s = input().split()
    name, l = s[0], s[1:]
    d[name] = set()
    for i in l:
        d[name].add(f[i])

for i in range(k):
    l = input().split()
    s = d[l[0]]
    for i in l[1:]:
        s = s.intersection(d[i])
    if len(s) == 0:
        print("None")
    else:
        print(*sorted([i for i in s]))
