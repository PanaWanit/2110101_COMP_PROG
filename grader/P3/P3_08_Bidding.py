d, D, SUM, last = dict(), dict(), dict(), dict()
for T in range(int(input())):
    s = input().split()
    if len(s) == 4: #B
        name, product = s[1],s[2]
        price = int(s[3])
        D[name], SUM[name] = [], 0
        if name in last : last[name][product] = (price, T)
        else : last[name] = {product: (price, T)}
        if product in d: d[product].append([-price, T, name])
        else: d[product] = [[-price, T, name]]
    else:
        name, product = s[1],s[2]
        last[name][product] = (0, 0)
for product in d.keys():
    for j in range(len(d[product])):
        name = d[product][j][2]
        d[product][j] = [-last[name][product][0], last[name][product][1], name]
for product, tmp in d.items():
    price, name = sorted(tmp)[0][::2]
    if last[name][product][0] == 0: continue
    if name in D:
        D[name].append(product)
        SUM[name] += -price
for name, val, l in sorted([[name, SUM[name], sorted(l)] for name, l in D.items()]):
    if val == 0:
        print(name+': ', '$', val, sep='')
    else:
        print(name+': ', '$', val, ' -> ', ' '.join(l), sep='')
