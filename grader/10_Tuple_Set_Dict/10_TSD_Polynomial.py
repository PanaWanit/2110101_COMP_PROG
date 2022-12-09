def add_dict(d, key, val):
    if key not in d:
        d[key] = 0
    d[key] += val

def add_poly(p1, p2):
    d = dict()
    for coefficient, power in p1:
        d[power] = coefficient
    for coefficient, power in p2:
        add_dict(d, power, coefficient) # d[power] += coefficient
    l = sorted([(-power, coefficient) for power, coefficient in d.items() if coefficient!=0])
    return [(a, -b) for b, a in l]

def mult_poly(p1, p2):
    d = dict()
    for coefficient_1, power_1 in p1:
        for coefficient_2, power_2 in p2:
            add_dict(d, power_1+power_2, coefficient_1*coefficient_2)
    l = sorted([(-power, coefficient) for power, coefficient in d.items() if coefficient!=0])
    return [(a, -b) for b, a in l]

for i in range(3):
    exec(input().strip())
