class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        #self.value = value


ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
cards = []

deck_of_cards():
    for rank in ranks:
        for suit in suits:
            a = rank
            b = suit
            if ranks.index(a) == 0:
                c = 11
            elif ranks.index(a) > 9:
                c = 10
            else:
                c = ranks.index(a) + 1
            new_card = (a, b, c)
            cards.append(new_card)

#print(cards)

