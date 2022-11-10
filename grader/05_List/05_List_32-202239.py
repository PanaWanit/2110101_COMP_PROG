n = int(input())
now = int(input().split()[1])
q = []

sum_t=0
c=0
last=[]

for i in range(n-1):
    opr = input().split()
    if opr[0] == 'new':
        q.append([now, int(opr[1])])
        print('ticket', now)
        now+=1
    elif opr[0]=='next':
        last = q.pop(0)
        print('call', last[0])
    elif opr[0]=='order':
        dt = int(opr[1])-last[1]
        print('qtime', last[0], dt)
        sum_t += dt
        c+=1
    elif opr[0]=='avg_qtime':
        print('avg_qtime', round(sum_t/c, 4))



