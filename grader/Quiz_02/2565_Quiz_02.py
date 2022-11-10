def compare(a, pattern) :
    if len(a)-1 != len(pattern):
        return False
    if a[-1] != '/':
        return False
    for i in range(len(a)-1):
        if pattern[i] == '?':
            continue
        if pattern[i].lower() != a[i].lower():
            return False
    return True

def human_split(tmp):
    a = tmp[:].strip()
    l = []
    s=""
    if a[0] == '/':
        l.append('/')
        a = a[1:]
    for i in a:
        if i=='/':
            l.append(s+'/')
            s=""
        else:
            s += i
    if(s!=''):
        l.append(s)
    return l

file = open(input(), "r")
pattern = input()
new_name = input()

for line in file.readlines():
    l = human_split(line)
    for i in range(len(l)):
        if(not compare(l[i], pattern)):
            continue
        l[i] = new_name+'/'
    print(*l, sep='')
