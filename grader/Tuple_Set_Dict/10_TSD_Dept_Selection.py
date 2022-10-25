
d = {}

for i in range(int(input())):
    a,b = input().split()
    d[a] = int(b)

l = {}
score = []
id_s = []
for i in range(int(input())):
    s = input().split()
    l[s[0]] = s[2:]
    score.append((float(s[1]), s[0]))
    id_s.append(s[0])

score.sort(reverse=True)
id_s.sort()

fac = {}

for sc, i in score:
    for j in l[i]:
        if d[j]!=0:
            d[j] -= 1
            fac[i] = j
            break

for i in id_s:
    print(i, fac[i])
