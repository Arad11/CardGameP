import random
from Card import Card


class Deckofcards:
    def __init__(self, sum_cards=13):
        self.package = []
        for i in range(1, sum_cards):
            self.package.append(Card(i, 'diamond'))
            self.package.append(Card(i, 'spade'))
            self.package.append(Card(i, 'heart'))
            self.package.append(Card(i, 'club'))

    def __str__(self):
        return f"the package is {self.package}"

    def show(self):
        return f"the package is {self.package}"

    def shuffle_the_pack(self):
        random.shuffle(self.package)
        return self.package

    def deal_one(self):
        if len(self.package) > 1:
            rand_num = random.randint(0, len(self.package) - 1)
            return self.package.pop(rand_num)
        elif len(self.package) == 1:
            return self.package.pop()
        else:
            raise IndexError("invalid range! there aren't cards in the package")