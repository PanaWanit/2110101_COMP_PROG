def total(pocket):
    return sum(pocket[i] * i for i in pocket)

def take(pocket, money_in):
    for i in money_in:
        if i in pocket:
            pocket[i] += money_in[i]
        else:
            pocket[i] = money_in[i]

def pay(pocket, amt):
    p = {}
    tmp = pocket.items()
    tmp = sorted(tmp)[::-1] # auto sort dict is shit
    for a,b in tmp:
        if amt >= a:
            p[a] = min(amt//a, pocket[a])
            amt -= p[a]*a
    if amt != 0:
        return {}
    for i in p:
        pocket[i] = pocket[i] - p[i]
    return p

exec(input().strip())
