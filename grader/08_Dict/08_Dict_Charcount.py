d = {}
for c in input():
    if not c.isalpha():
        continue
    if c.lower() in d:
        d[c.lower()] -= 1
    else:
        d[c.lower()] = -1
for a,b in sorted([(x, y) for y, x in d.items()]):
    print(b, "->", -a)
