al = []
def ally(l):
    for country in l:
        for i in range(len(al)):
            if country in al[i]:
                al[i] = al[i].union(set(l))
                return
    al.append(set(l))
    return

def now_team(a):
    for i in range(len(al)):
        if a in al[i]:
            return i
    return -1

enemy_matrix = [ [0 for j in range(100)] for i in range(100) ]
def enemy(a, b):
    ally([a])
    ally([b])
    ia, ib = now_team(a), now_team(b)
    enemy_matrix[ia][ib] = enemy_matrix[ib][ia] = 1
    return


def table(l):
    for i in range(len(l)):
        a,b = l[i], l[i-1]
        ta,tb = now_team(a), now_team(b)
        if ta == -1 or tb == -1: # no team
            continue
        if enemy_matrix[ta][tb]:
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
