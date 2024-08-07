from carddeck import CardDeck
from card import Card

class JokerDeck(CardDeck):
    def _make_deck(self):
        super()._make_deck()
        for joker_number in range(1, 3):
            card = Card(f"Joker{joker_number}", f"Joker{joker_number}")
            self._cards.append(card)

if __name__ == "__main__":
    j = JokerDeck()
    j.shuffle()
    print(j.cards)
    print()
    for _ in range(5):
        print(j.draw())
    print(j)
    print(f"{j = }")
    print(f"{len(j) = }")
    