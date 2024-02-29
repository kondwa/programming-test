import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

class Deck:
    def __init__(self):
        self.cards = []
        self.populate()

    def populate(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None

    def cards_left(self):
        return len(self.cards)

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        self.cards.remove(card)

    def show_hand(self):
        for card in self.cards:
            print(f"{card.rank} of {card.suit}")

# Example usage:
deck = Deck()
deck.shuffle()
hand = Hand()

print("Drawing 5 cards:")
for _ in range(5):
    card = deck.draw()
    if card:
        hand.add_card(card)
    else:
        print("No more cards left in the deck!")
        break

print("Cards in hand:")
hand.show_hand()

print(f"\nNumber of cards left in the deck: {deck.cards_left()}")
