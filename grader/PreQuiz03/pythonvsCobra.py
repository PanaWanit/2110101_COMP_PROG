member_list = dict()
score_count = dict()
get_group = dict()
vote_list = dict()
get_index = {'Y':0, 'X':1, 'N':2}

group_list = [input() for i in range(int(input()))]
for s in group_list:
    member_list[s] = list()
    score_count[s] = [0, 0, 0]

for i in range(int(input())):
    name, g = input().split()
    get_group[name] = g

for i in range(int(input())):
    name, vote = input().split()
    vote_list[name] = get_index[vote]
    g = get_group[name]
    member_list[g].append(name) # collect only member who voted
    score_count[g][get_index[vote]] += 1

for group in group_list:
    print(group)
    sorted_score = sorted(score_count[group], reverse=True)
    if sorted_score[0] == sorted_score[1]: # have 2 max_score #include that max_score == 0
        print("Inconclusive")
        continue
    winner = score_count[group].index(sorted_score[0]) #find max_score index
    cobra = sorted([member for member in member_list[group] if vote_list[member] != winner])
    if len(cobra) != 0:
        print(*cobra, sep=', ')
    else:
        print('No cobra')
