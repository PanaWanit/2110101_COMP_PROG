d,m,y = map(int, input().split('/'))
print(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'][m-1],\
        str(d)+",", y)

