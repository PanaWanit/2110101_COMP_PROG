i=1
m = int(input())
cx,cy=0,0

for i in range(3*m):
    x,y = input().split()

    if x=='R':
        if y=='P':
            cy+=1
        if y=='S':
            cx+=1
    if x=='P':
        if y=='S':
            cy+=1
        if y=='R':
            cx+=1
    if x=='S':
        if y=='R':
            cy+=1
        if y=='P':
            cx+=1
    if cx == m:
        print(cx, cy, '\nPlayer 1 wins')
        quit()
    if cy == m:
        print(cx, cy, '\nPlayer 2 wins')
        quit()
print(cx, cy, '\nTie')


