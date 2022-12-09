al = []
def ally(l):
    for country in l:
        for i in range(len(al)):
            if country in al[i]:
                al[i] = al[i].union(set(l))
                return
    al.append(set(l))
    return

d = dict()
def enemy(a, b):
    ally([a])
    ally([b])
    if a not in d:
        d[a] = set()
    if b not in d:
        d[b] = set()
    d[a].add(b)
    d[b].add(a)
    return

def now_team(a):
    for i in range(len(al)):
        if a in al[i]:
            return i
    return -1

def table(l):
    for i in range(len(l)):
        a,b = l[i], l[i-1]
        ta,tb = now_team(a), now_team(b)


        if ta == -1 or tb == -1: # no team
            continue
        if ta == tb: #same team
            continue
        for now, enemy_list in d.items():
            if now_team(now) == ta: # same team with a
                for c in enemy_list:
                    if now_team(c) == tb:
                        return False
            if now_team(now) == tb: # same team with a
                for c in enemy_list:
                    if now_team(c) == ta:
                        return False

    return True


while True:
    s = input().split()
    if s[0]=='End': break
    if s[0] == 'Ally':
        ally(s[1:])
    elif s[0] == 'Enemy':
        enemy(s[1], s[2])
    elif s[0] == 'Table':
        print('Okay' if table(s[1:]) else 'No')
