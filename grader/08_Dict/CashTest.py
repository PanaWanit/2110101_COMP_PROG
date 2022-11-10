def total(pocket):
    t = 0
    for i in pocket:
        t += i*pocket[i]
    return t
def take(pocket, money_in):
    for i in money_in:
        if i in pocket:
            pocket[i] += money_in[i]
        else:
            pocket[i] = money_in[i]
    return pocket
def pay(pocket, amt):
    a = amt
    p = {}
    npocket = {}
    for i in pocket:
        npocket[i] = pocket[i]
    while a != 0:
        mx = 0
        ch = 0
        for i in npocket:
            if i > mx and i <= a and npocket[i] > 0:
                mx = i
                ch = 1
        if ch == 0:
            return {}
        npocket[mx] -= 1
        a -= mx
        if mx in p:
            p[mx] += 1
        else:
            p[mx] = 1
    for i in npocket:
        pocket[i] = npocket[i]
    print(len(p))
    return p
exec(input().strip())