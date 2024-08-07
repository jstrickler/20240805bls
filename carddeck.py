import random
from card import Card

class CardDeck:
    RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()
    SUITS = "Clubs Diamonds Hearts Spades".split()

    # constructor
    def __init__(self):
        self._make_deck()

    # private instance method
    def _make_deck(self):
        self._cards = list()
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)
    
    @property
    def cards(self):
        return self._cards

    # instance method
    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    @classmethod
    def get_ranks(cls):
        return cls.RANKS

    def __str__(self):
        my_type = type(self)
        my_name = my_type.__name__
        return f"{my_name}:{len(self)}"

    def __repr__(self):
        my_type = type(self)
        my_name = my_type.__name__
        return f"{my_name}()"

    def __len__(self):
        return len(self._cards)

if __name__ == "__main__":
    d1 = CardDeck()
    print(f"{d1 = }")
    print(d1)
    d1.shuffle()   #    instance.method()
    print(f"{d1.cards = }")
    for _ in range(5):
        print(d1.draw())
    
    d2 = CardDeck()
    print(f"{d2.get_ranks() = }")
    print(f"{CardDeck.get_ranks() = }")
    print(CardDeck.__len__(d1))
    print(f"{d1.__len__() = }")
    print(len(d1))