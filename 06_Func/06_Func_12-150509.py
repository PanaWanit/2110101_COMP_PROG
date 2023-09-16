
def is_prime(n):
    sq = int(n**0.5)
    if n <= 1:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

def next_prime(n):
    n += 1
    while True:
        if is_prime(n):
            return n
        n+=1

def next_twin_prime(n):
    a = next_prime(n)
    b = next_prime(a)
    while b-a!=2:
        a = b
        b = next_prime(a)
    return (a, b)

exec(input().strip())
