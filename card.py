"""
Provide Card class

Syntax:
c = Card("rank", "suit")
"""
class Card:   # inherits from 'object'
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    def get_rank(self):   #  self is like 'this' in Java/C#
        return self._rank

    @property
    def rank(self):
        return self._rank
    
    @property
    def suit(self):
        return self._suit
    
    def __str__(self):  #  human friendly version of object
        return f"Card:{self.rank}-{self.suit}"
    
    def __repr__(self):  # how to recreate the object
        return f"Card('{self.rank}', '{self.suit}')"

if __name__ == "__main__":
    c = Card("2", "Clubs")
    print(c)    
    print(f"{c.rank = }")  # calls c.rank() (kinda)
    print(f"{c.suit = }")
    c2 = Card("10", "Diamonds")
    print(c2)  # uses str()

    print(f"{c = }")   # uses repr()

    
