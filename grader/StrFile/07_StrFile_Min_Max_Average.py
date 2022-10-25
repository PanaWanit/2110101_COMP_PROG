f,y = input().split()

f = open(f, 'r')

t = f.readline()

mn = 10000000; mx = 0
l = []
while t!="":
    i,s = t.split()
    s = float(s)
    if i[0:2] != y[2:]:
        t = f.readline()
        continue
    mx = max(mx, s)
    mn = min(mn, s)
    l.append(s)
    t = f.readline()
if len(l)==0:
    print("No data")
    quit()
print(mn, mx, sum(l)/len(l))
