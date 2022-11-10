opr = input()
n = int(input())
a = [[x for x in input()]]
m = len(a[0])
valid = True

for i in range(n-1):
    a.append([x for x in input()])
    if len(a[-1]) != m:
        valid = False

if valid==False:
    print("Invalid size")
    quit()

if opr=='90':
    for i in range(m):
        for j in range(n):
            print(a[n-j-1][i], end='')
        print()
if opr=='180':
    for i in range(n):
        for j in range(m):
            print(a[n-i-1][m-j-1], end='')
        print()
if opr=='flip':
    for i in range(n):
        for j in range(m):
            print(a[i][m-j-1], end='')
        print()
