l, y = input().split()

l = open(l, 'r').readlines()

mn = 1e9; mx=0; 
nisit = []
for line in l:
    _id, score = line.split()
    if y[2:] != _id[:2]:
        continue
    score = float(score)
    nisit.append(score)
    mx = max(mx, score)
    mn = min(mn, score)

if len(nisit)==0:
    print("No data")
else:
    print(mn, mx, sum(nisit)/len(nisit))

