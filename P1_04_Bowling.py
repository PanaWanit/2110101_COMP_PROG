s = input()
frame = []
i=0
while i < len(s):

    if len(frame)==9:
        t = []
        for x in s[i:]:
            if x == 'X':
                t.append(10)
            elif x == '/':
                t.append(10-t[len(t)-1])
            else:
                t.append(int(x))
        frame.append(t)
        break
    elif s[i] == 'X':
        frame.append([10])
        i+=1
    elif '0' <= s[i] <= '9' and s[i+1]=='/':
        frame.append([int(s[i]), 10-int(s[i])])
        i+=2
    else:
        frame.append([int(s[i]), int(s[i+1])])
        i+=2

frame_list = [x for i in frame for x in i]
frame_size = [len(x) for x in frame]
frame_list.append(0)

now = 0
score = []

for i in range(9):
    s = sum(x for x in frame[i])
    if s==10:
        if len(frame[i])==1:
            s += frame_list[now+len(frame[i])] + frame_list[now+len(frame[i])+1]
        else:
            s += frame_list[now+len(frame[i])]
    now += frame_size[i]
    score.append(s)
score.append(sum(x for x in frame[9]))

t = int(input())
if 1 <= t <= 10:
    print(score[t-1])
else:
    print(sum(x for x in score))
