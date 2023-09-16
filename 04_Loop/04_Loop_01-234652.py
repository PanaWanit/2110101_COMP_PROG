s,c=0,0
x = input()
while x != 'q':
    s += float(x)
    x = input()
    c +=1
print(round(s/c, 2) if c!=0 else "No Data")
