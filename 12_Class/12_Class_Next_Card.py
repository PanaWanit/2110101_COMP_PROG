l_card = ["3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A", "2"]
l_suit = ['club', 'diamond', 'heart', 'spade']
precision_score = {val: index for index, val in enumerate(l_card)}
precision_suit = {val: index for index, val in enumerate(l_suit)}
class Card:
    def __init__(self, value, suit):
        self.val = value
        self.suit = suit

    def __str__(self):
        return '({} {})'.format(self.val, self.suit)
    def add(self, x):
        now = (precision_score[self.val] * 4 + precision_suit[self.suit] + x)%52
        return Card(l_card[now//4], l_suit[now%4])

    def next1(self):
        return self.add(1)
    def next2(self):
        res = self.add(1)
        self.val, self.suit = res.val, res.suit

n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))

for i in range(n):
    print(cards[i].next1())

print("----------")

for i in range(n):
    print(cards[i])

print("----------")

for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i])
