def missing_digits(t):
    a=[]
    for i in range(10):
        if str(i) not in t:
            a.append(i)
    return a
exec(input())
