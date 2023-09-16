idx_idol, voter_score, idol_score, idol_count, kami_score = dict(), dict(), dict(), dict(), dict()

def add_dict(d, key, val):
    if key in d: d[key] += val
    else: d[key] = val

x, T = input(), 1
while x not in "123":
    voter, idol, score = x.split(); score = int(score)
    if idol not in idx_idol: idx_idol[idol] = T #set first index of idol

    add_dict(idol_score, idol, score) # idol_score[idol] += score
    
    kami_score[idol] = 0

    if idol not in idol_count : idol_count[idol] = {voter} # unique voter
    else: idol_count[idol].add(voter)

    if voter not in voter_score:
        voter_score[voter] = {idol: score}
    else:
        add_dict(voter_score[voter], idol, score) # voter_score[voter][idol] += score

    x = input(); T+=1
for voter in voter_score.keys():
    mx,kami_oshi = 0, ""
    for idol in voter_score[voter]:
        if voter_score[voter][idol] > mx:
            mx, kami_oshi = voter_score[voter][idol], idol
        if voter_score[voter][idol] == mx and idol < kami_oshi: kami_oshi = idol
    add_dict(kami_score, kami_oshi, 1)

if x=='1':      l = sorted([(-idol_score[idol], idx_idol[idol], idol) for idol in idol_score.keys()])
elif x=='2':    l = sorted([(-len(idol_count[idol]), idx_idol[idol], idol) for idol in idol_score.keys()])
else:           l = sorted([(-kami_score[idol], idx_idol[idol], idol) for idol in idol_score.keys()])
print( ', '.join([x[2] for x in l][:3]) )
