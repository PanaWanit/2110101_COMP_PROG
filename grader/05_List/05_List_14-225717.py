def peaks(x):
    c=0
    for i in range(1, len(x)-1):
        if x[i] > x[i-1] and x[i] > x[i+1]:
            c+=1
    return c
print(peaks(list(map(float, input().split()))))
