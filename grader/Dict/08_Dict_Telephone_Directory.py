d = {}
for i in range(int(input())):
    s = input()
    tel = s.split()[2]
    name = ' '.join(s.split()[:2])
    d[name] = tel
    d[tel] = name

for i in range(int(input())):
    s = input()
    if s in d:
        print(s, '-->', d[s])
    else:
        print(s, '--> Not found')

