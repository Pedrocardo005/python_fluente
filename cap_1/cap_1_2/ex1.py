import collections
from random import choice

# Cria uma classe de uma maneira simples, servindo apenas para armazenar
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        # Como se criasse o for ranks dentro do for suits
        self._cards = [Card(rank, suit)
                       for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    # Modificado
    def todos(self):
        return self._cards


beer_card = Card('7', 'diamonds')
print(beer_card)
deck = FrenchDeck()
print(len(deck))

print(deck[0])
print(deck[-1])

# from random import choice
# Devolve um item aleatório
print(choice(deck))
print(choice(deck))
print(choice(deck))

# Pegando as três primeiras cartas
print(deck[:3])
# Pegando o índice 12 e pulando de 13 em 13
print(deck[12::13])

print('Imprimindo baralho completo')
for card in deck:
    print(card)

print('\nImprimindo na ordem inversa')
for card in reversed(deck):
    print(card)

print('\nVerifica se contém')
print(Card('Q', 'hearts') in deck)
print(Card('7', 'beasts') in deck)

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


print('\nImprime ordenado')
for card in sorted(deck, key=spades_high):
    print(card)
