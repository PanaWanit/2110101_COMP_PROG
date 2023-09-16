n = int(input())
mn,mx= 10**9, -10**9
mnn,mxx= 10**9, -10**9
for i in range(n):
    a = list(map(int, input().split()))
    mn = min(mn, a[i%2])
    mxx = max(mxx, a[i%2])
    mx = max(mx, a[1-i%2])
    mnn = min(mnn, a[1-i%2])
print(str(mn)+' '+str(mx) if input()=="Zig-Zag" else str(mnn) + ' ' + str(mxx))
