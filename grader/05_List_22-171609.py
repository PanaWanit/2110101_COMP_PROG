x = input()

def up(x):
    if x=='A':
        return 'A'
    if x=='B+':
        return 'A'
    if x=='B':
        return 'B+'
    if x=='C+':
        return 'B'
    if x=='C':
        return 'C+'
    if x=='D+':
        return 'C'
    if x=='D':
        return 'D+'
    if x=='F':
        return 'D'
student = []
while x!='q':
    student.append(x.split())
    x = input()
ans=[]
for l in input().split():
    for x in student:
        if x[0]==l:
            x[1] = up(x[1])
for i in sorted(student):
    print(' '.join(i))
