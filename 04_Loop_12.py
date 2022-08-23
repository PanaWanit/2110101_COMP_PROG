mn,mx= 10**9, -10**9
mnn,mxx= 10**9, -10**9
i=0
s = input()
while s != 'Zig-Zag' and s!= 'Zag-Zig':
    a = list(map(int, s.split()))
    mn = min(mn, a[i%2])
    mxx = max(mxx, a[i%2])
    mx = max(mx, a[1-i%2])
    mnn = min(mnn, a[1-i%2])
    s = input()
    i+=1
print(str(mn)+' '+str(mx) if s=="Zig-Zag" else str(mnn) + ' ' + str(mxx))
