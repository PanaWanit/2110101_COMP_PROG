d = dict()
def valid(s):
    cnt = dict()
    for i in s.split():
        if i not in d:
            return False
        if d[i] in cnt:
            return False
        cnt[d[i]] = 1
    return True

for _ in range(int(input())):
    team, country = input().split()
    d[team] = country

while True:
    s = input()
    if s == 'q':
        break
    print('OK' if valid(s) else 'Not OK')
