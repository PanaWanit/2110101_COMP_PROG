def isPrime(n):
    sq = int(n**0.5)
    for i in range(2, sq):
        if n%i==0:
            return False
    return True

def factor(n):
    if n<=1:
        return [n,1]
    sq = int(n**0.5)
    l=[]
    for i in range(2, sq+1):
        if not isPrime(i):
            continue
        c=0;
        while n%i==0:
            n//=i
            c+=1;
        if c==0:
            continue
        l.append([i, c])
    if n!=1:
        l.append([n, 1])
    return l

exec(input().strip())
