def add_dict(d, key, val):
    if key in d: d[key] += val
    else: d[key] = val

group_list = [input() for i in range(int(input()))]

x_cnt, y_cnt, z_cnt = dict(), dict(), dict()
which_group = dict()

for i in group_list:
    x_cnt[i] = 0
    y_cnt[i] = 0
    z_cnt[i] = 0

for i in range(int(input())):
    name, group = input().split()
    which_group[name] = group


list_vote = dict()
member_vote = dict()
for i in range(int(input())):
    name, vote = input().split()
    group = which_group[name]
    if group not in member_vote: member_vote[group] = []
    if group not in list_vote : list_vote[group] = []
    member_vote[group].append(name)
    if vote == 'X':
        x_cnt[group] += 1
    if vote == 'Y':
        y_cnt[group] += 1
    if vote == 'N':
        z_cnt[group] += 1
    list_vote[name] = vote

for group in group_list:
    print(group)
    if x_cnt[group] > max(y_cnt[group], z_cnt[group]):
        now = 'X'
        ans = []
        for i in member_vote[group]:
            if list_vote[i] != now:
                ans.append(i)
        if(len(ans)==0): print("No cobra")
        else:  print(', '.join(sorted(ans)))
    elif y_cnt[group] > max(x_cnt[group], z_cnt[group]):

        now = 'Y'
        ans = []
        for i in member_vote[group]:
            if list_vote[i] != now:
                ans.append(i)
        if(len(ans)==0): print("No cobra")
        else:  print(', '.join(sorted(ans)))
    elif z_cnt[group] > max(x_cnt[group], y_cnt[group]):

        now = 'N'
        ans = []
        for i in member_vote[group]:
            if list_vote[i] != now:
                ans.append(i)
        if(len(ans)==0): print("No cobra")
        else:  print(', '.join(sorted(ans)))
   # elif x_cnt[group] == y_cnt[group] or x_cnt[group] == z_cnt[group] or y_cnt[group] == z_cnt[group]:
   #     print("Inconclusive")
    else:
       print("Inconclusive")

