a = input()
b = input()

if len(a) != len(b):
    print("Incomplete answer")
    quit()

c=0
for i in range(len(a)):
    if a[i] == b[i]:
        c+=1
print(c)

