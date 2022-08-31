def peaks(x):
    a=[]
    for i in range(1, len(x)-1):
        if x[i] > x[i-1] and x[i] > x[i+1]:
            a.append(i)
    return a
exec(input())
