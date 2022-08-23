def inp():
    s = input()
    return s.split(', ')[0].split() + [int(s.split(', ')[1])]
month = {'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6, 'July':7, 'August':8, 'September':9, 'October':10, 'November':11, 'December':12}

x = inp()
y = inp()
if x[1:] == y[1:]:
    print(x[0], y[0])
elif x[3] < y[3] or month[x[1]] < month[y[1]] or int(x[2]) < int(y[2]):
    print(x[0])
else:
    print(y[0])
