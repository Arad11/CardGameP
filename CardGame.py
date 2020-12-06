from OurProject.Deckofcards import Deckofcards
from OurProject.Card import Card
from OurProject.Player import Player
import random

class CardGame:
    def __init__(self, name1, name2, numcards=10):
        """
        פעולה שיוצרת משחק קלפים
        """
        self.deck = []
        player1 = Player(name1, numcards)
        player2 = Player(name2, numcards)
        self.player1 = player1
        self.player2 = player2
        self.was_new_game_called = False
        self.new_game(numcards)

    def __str__(self):
        return f'player1 {self.player1} \n player2 {self.player2}'

    def new_game(self, cardsnum):
        """
        פעולה שמאתחלת משחק חדש
        """
        if self.was_new_game_called == False:
            deck = Deckofcards().shuffle_the_pack()
            self.deck = deck
            self.player1.set_hand(self.deck, cardsnum)
            self.player2.set_hand(self.deck, cardsnum)
            self.was_new_game_called = True


    def get_winner(self):
        """
        פעולה שבודקת למי יש חבילה גדולה יותר והוא יהיה המנצח
        """
        if len(self.player1.pack) > len(self.player2.pack):
            return f"the winner is {self.player1.name}"
        elif len(self.player1.pack) < len(self.player2.pack):
            return f"the winner is {self.player2.name}"
        else:
            return None