def gcd(a, b):
    while b!=0:
        a,b = b, a%b
    return a

def is_coprime(a, b, c):
    return gcd(gcd(a, b), c)==1

def primitive_Pythagorean_triples(max_len):
    l=[]
    for k in range(3, max_len+1):
        for i in range(1, k-1):
            for j in range(i+1, k):
                if is_coprime(i, j, k) and i**2 + j**2 == k**2:
                    l.append([i, j, k])
    return l

exec(input().strip())
