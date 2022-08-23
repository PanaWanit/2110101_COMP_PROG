n = int(input())
l = []
def dist(x, y):
    return (x**2+y**2)**0.5
for i in range(n):
    l.append(list(map(float, input().split())))
    l[i].insert(0, dist(l[i][0], l[i][1]))
    l[i].insert(1, i+1)
l = sorted(l)
print("#{}: m ({}, {})".format(l[2][1], l[2][2], l[2][3]))
