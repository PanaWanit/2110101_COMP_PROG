def f1(a, b, c):
    if a<=0: a=1000000
    if b<=0: b=1000000
    if c<=0: c=1000000
    return min(a, b, c)

def f2(a, b, c):
    if a>=0: a=-1000000
    if b>=0: b=-1000000
    if c>=0: c=-1000000
    return max(a, b, c)

def f3(a, b, c):
    return int(str(abs(a+b+c))[0])

def f4(a, b, c):
    return int(str(abs(a+b+c))[-1])

def main():
    s1, s2, a, b, c = [int(e) for e in input().split()]
    if s1==0 and s2==0:
        print(f1(a, b, c))
    elif s1==0 and s2==1:
        print(f2(a, b, c))
    elif s1==1 and s2==0:
        print(f3(a, b, c))
    elif s1==1 and s2==1:
        print(f4(a, b, c))
    else:
        print("Error")
exec(input().strip())
