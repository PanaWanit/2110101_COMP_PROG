h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())
MOD = 24*60*60
t = ((h2*3600 + m2*60 + s2) - (h1*3600 + m1*60 + s1))%MOD
t = (t+MOD)%MOD
dh,dm,ds = t//3600, t%3600//60, t%60
print(str(dh)+":"+str(dm)+":"+str(ds))
