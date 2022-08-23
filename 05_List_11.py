cnt = [0]*10
for x in input():
    if '0' <= x <= '9':
        cnt[int(x)]+=1
a = []
for i in range(10):
    if cnt[i]==0:
        a.append(i)
print(','.join(map(str, a)) if len(a)!= 0 else 'None')
