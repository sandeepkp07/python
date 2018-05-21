import random
class Cards(object):
 
	suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
 	rank_names = [None, "Ace", "2", "3", "4", "5", "6", "7","8", "9", "10", "Jack", "Queen", "King"]

	def __init__(self,suit=0,rank=2):
		self.suit = suit
		self.rank = rank
 
	def __str__(self):
		return ('%s of %s' % (Cards.rank_names[self.rank],Cards.suit_names[self.suit]))

	def __cmp__(self,other):
  		t1 = self.suit,self.rank
		t2 = other.suit,other.rank
		return cmp(t1,t2)

class Deck(Cards):
	def __init__(self):
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Cards(suit,rank)
				self.cards.append(card)

	def __str__(self):
		res = []
		for cards in self.cards:
   			res.append(str(cards))
  		return '\n'.join(res)
	def pop_card(self):
		return self.cards.pop()
	def add_card(self,card):
		self.cards.append(cards)
	def shuffle(self):
		random.shuffle(self.cards)
	def sort(self):
		self.cards.sort()
deck = Deck()
deck.shuffle()
deck.sort()
print (deck)
