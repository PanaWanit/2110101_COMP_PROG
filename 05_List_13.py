n = int(input())
a = []
i=0
for k in range(n):
    if i%2==0:
        a.append(int(input()))
    else:
        a.insert(0, int(input()))
    i+=1
x = list(map(int, input().split()))
for k in range(len(x)):
    if i%2==0:
        a.append(x[k])
    else:
        a.insert(0, x[k])
    i+=1

y = int(input())
while y!=-1:
    if i%2==0:
        a.append(y)
    else:
        a.insert(0, y)
    i+=1
    y = int(input())
print(a)
