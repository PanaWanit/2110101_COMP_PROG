l = []
for i in range(int(input())):
    s = input()
    l.append((s.split()[0], set([x for x in s.split()[1:]]), s.split()))

l.sort()

target = input().split()

ans=0
for i in l:
    ch=1
    for j in target:
        if j not in i[1]:
            ch=0
            break
    if ch==1:
        ans = 1
        print(" ".join(i[2]))
if ans==0:
    print("Not Found")
