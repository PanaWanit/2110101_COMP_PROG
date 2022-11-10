d = {}
s = {}
sm = 0.0
for i in range(int(input())):
    a,b = input().split()
    b = int(b)
    d[a] = b
    s[a] = 0


for i in range(int(input())):
    a,b = input().split()
    b = int(b)
    if a not in d:
        continue
    sm += b*d[a]
    s[a] -= b*d[a]

if sm==0:
    print("No ice cream sales")
    quit()

s = sorted([(b, a) for a,b in s.items()])

print("Total ice cream sales:", sm)
print("Top sales:", ', '.join([a for b, a in s if b==s[0][0]]))
