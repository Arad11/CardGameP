from Card import Card
import random


class Player:
    def __init__(self, name, pack=10):
        self.name = name
        self.pack = []

    def __str__(self):
        return f'{self.name} have the package {self.pack}'

    def show(self):
        return f'{self.name} have the package {self.pack}'

        """
        פעולה שמחלקת לשחקן חבילת קלפים חדשה
        """
    def set_hand(self, cardsnum, deck):
        if not isinstance(deck, list):
            raise TypeError("invalid number. insert list")
        else:
            for i in deck:
                if type(i) != Card:
                    raise TypeError("you can only insert Cards to the deck!")

        if type(cardsnum) is not int:
            raise TypeError("invalid value. insert number")
        if cardsnum < 1 or cardsnum > len(deck):
            raise IndexError("invalid number. insert number between 1 and package length")
        for i in range(0, cardsnum):
            self.pack.append(deck.pop(i))
        return self.pack

    def get_random_card(self):
        """
        פעולה שבוחרת קלף מחבילה של השחקן מוציאה אותו בלי להחזיק לחבילה
        """
        packlen = len(self.pack)
        if packlen > 1:
            randnum = random.randint(0, packlen - 1)
            return self.pack.pop(randnum)
        elif packlen == 1:
            return self.pack.pop()
        else:
            raise IndexError("invalid range! there aren't cards in the package")

    def add_card(self, newcard='nothing added'):
        """
        פעולה שמוסיפה קלף לחבילה של שחקן מסוים"""
        if newcard == 'nothing added':
            raise ValueError("invalid value. Must insert a new Card!")
        if type(newcard) is not Card:
            raise TypeError("invalid value. Must insert Card!")
        return self.pack.append(newcard)
