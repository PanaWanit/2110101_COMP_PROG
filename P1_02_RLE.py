op = input()

if op=="str2RLE":
    x = input()
    x += '\\'
    c=1
    for i in range(1, len(x)):
        if x[i] != x[i-1]:
            print(x[i-1], c)
            c=0
        c+=1

elif op=='RLE2str':
    x = input().split()
    for i in range(0, len(x), 2):
        print(x[i] * int(x[i+1]), end='')
else:
    print("Error")
