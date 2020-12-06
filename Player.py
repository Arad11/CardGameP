from Deckofcards import Deckofcards
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

    def set_hand(self, deck, cardsnum):
        """
        פעולה שמחלקת לשחקן חבילת קלפים חדשה
        """
        if not isinstance(deck,list):
            print("invalid number. insert list")
            return None
        # else:
        #     for i in range(len(deck)):
        #         if not type(deck[i]) is not Card:
        #             print("in the package the values must be cards1")
        #             return None

        if type(cardsnum) is not int:
            print("invalid value. insert number")
            return None
        if cardsnum < 1 or cardsnum > len(deck):
            print("invalid number. insert number between 1 and package length")
            return None
        for i in range(0, cardsnum):
            self.pack.append(deck.pop(i))
        return self.pack

    def get_random_card(self):
        """
        פעולה שבוחרת קלף מחבילה של השחקן מוציאה אותו בלי להחזיק לחבילה
        """
        packlen = len(self.pack)
        if packlen == 1:
            return self.pack.pop()
        else:
            randnum = random.randint(0, packlen - 1)
            return self.pack.pop(randnum)

    def add_card(self, newcard):
        """
        פעולה שמוסיפה קלף לחבילה של שחקן מסוים
        """
        kind = {1: 'diamond', 2: 'spade', 3: 'heart', 4: 'club'}
        c ={newcard.value: kind[newcard.suit]}
        self.pack.append(c)
        return self.pack