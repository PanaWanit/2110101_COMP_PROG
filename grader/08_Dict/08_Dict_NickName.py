d = {}
for i in range(int(input())):
    a,b = input().split()
    d[a] = b
    d[b] = a

for i in range(int(input())):
    s = input()
    if s in d:
        print(d[s])
    else:
        print("Not found")

