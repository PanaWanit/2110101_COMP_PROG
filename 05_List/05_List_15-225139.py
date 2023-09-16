x = sorted(list(map(int, input().split())))+['k']
a = []

for i in range(1, len(x)):
    if x[i] != x[i-1]:
        a.append(x[i-1])
print(len(a))
print(a[:10])
