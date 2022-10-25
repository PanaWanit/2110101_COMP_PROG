def mod(s):
    s.replace('\"', ' ')
    for i in s:
        if not i.isalnum():
            s=s.replace(i, ' ')
    return s
l = mod(input()).split()

print(l[0].lower(), end='')
for s in l[1:]:
    print(s.capitalize(), end='')
