s = input().upper()
o = input()

if any(c not in 'AGCT' for c in s):
    print("Invalid DNA")
    quit()

if o=='R':
    print(s.replace('A', 'a').replace('T', 'A').replace('a', 'T').replace('C', 'c').replace('G', 'C').replace('c', 'G')[::-1])
if o=='F':
    print('A=%d, T=%d, G=%d, C=%d' % (s.count('A'), s.count('T'), s.count('G'), s.count('C')))
if o=='D':
    x = input()
    c=0
    for i in range(len(s)-len(x)+1):
        if s[i:i+len(x)] == x:
            c+=1
    print(c)

