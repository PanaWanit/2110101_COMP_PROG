l_card = ["3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A", "2"]
precision_score = {val: index for index, val in enumerate(l_card)}
precision_suit = {'spade':3, 'heart':2, 'diamond':1, 'club':0}
class Card:
    def __init__(self, value, suit):
        self.val = value
        self.suit = suit

    def __str__(self):
        return '({} {})'.format(self.val, self.suit)

    def getScore(self):
        if self.val == 'A':
            return 1
        if self.val in 'JQK':
            return 10
        return int(self.val)

    def sum(self, other):
        return (self.getScore() + other.getScore())%10
    def __lt__(self, rhs):
        if precision_score[self.val] != precision_score[rhs.val]:
            return precision_score[self.val] < precision_score[rhs.val]
        return precision_suit[self.suit] < precision_suit[rhs.suit]

n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].getScore())
print("----------")
for i in range(n-1):
    print(Card.sum(cards[i], cards[i+1]))
print("----------")
cards.sort()
for i in range(n):
    print(cards[i])
