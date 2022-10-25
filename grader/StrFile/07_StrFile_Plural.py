s = input()

if s[-1] == 'y' and s[-2] not in 'aeiou':
    print(s[:-1] + 'ies')
elif s[-1] in 'sx' or s[-2:] == 'ch':
    print(s+'es')
else:
    print(s+'s')
