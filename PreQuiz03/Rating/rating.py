
data = dict() # Song Name : (Rating, SongLV, Score)

def cal_rating(score, song_lv):
    return int(25 * (song_lv+1) * (score/(10**7)))

def add_song(song_name, score_set):
    if song_name not in data:
        data[song_name] = score_set
    else:
        data[song_name] = max(data[song_name], score_set)

def get_rating_name(song_name):
    if song_name not in data:
        return 0
    return data[song_name][0]

def get_rating_score():
    return sum(sorted( [ get_rating_name(song_name) for song_name in data.keys() ])[-5:])

for _ in range(int(input())):
    inp = input().strip().split(' | ')
    if inp[0] == 'Play': # OPR | Song name | Song LV | Score
        song_name, song_lv, score = inp[1], int(inp[2]), int(inp[3])
        rating = cal_rating(score, song_lv)
        add_song(song_name, (rating, song_lv, score))
    elif inp[0] == 'Rating':
        if len(inp) == 1:
            print(get_rating_score())
        else:
            print(get_rating_name(inp[1]))
    else: #detail
        song_name = inp[1]
        if song_name not in data:
            print(song_name+': No play history')
        else:
            rating, song_lv, score = data[song_name]
            print(' | '.join(map(str, [song_name, song_lv, score, rating])))
