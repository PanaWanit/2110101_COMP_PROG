n = int(input())
l = []
d = {}
for i in range(n):
    a,b = input().split(": ")
    l.append(a)
    d[a] = set(b.split(", "))

target = input()
ch=0

for i in l:
    if i == target:
        continue
    for j in d[i]:
        if j in d[target]:
            print(i)
            ch=1
            break
if ch==0:
    print("Not Found")
    
