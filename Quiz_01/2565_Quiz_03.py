s = input()
a = s
b = s

a = a.replace('-', ' ')
a = a.replace('+', ' ')

l = [int(x) for x in a.split()]

sm = 0

if s[0] == '-':
    sm = -l[0]
else:
    sm = l[0]

i=1
for x in s[1:]:
    if x.isdigit():
        continue
    if x=='+':
        sm += l[i] 
    else:
        sm -= l[i]
    i+=1
print(sm)
