t = input()
s = input()
a = ""

for i in s:
    a += (i if i not in "\'\"(),.\'" else " ")

print(a.split().count(t))
