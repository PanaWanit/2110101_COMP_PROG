def distance1(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5
def distance2(p1, p2):
    return sum((p1[i]-p2[i])**2 for i in range(2))**0.5
def distance3(c1, c2):
    return distance2(c1[:2], c2[:2]), c1[2]+c2[2]>=distance2(c1[:2], c2[:2])
def perimeter(points):
    return sum(distance2(points[i], points[(i+1)%len(points)]) for i in range(len(points)))
exec(input().strip())
