from Deckofcards import Deckofcards
from Player import Player


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

    def new_game(self, cardsnum=10):
        """
        פעולה שמאתחלת משחק חדש
        """
        if type(cardsnum) is not int:
            raise ValueError("invalid value. insert number between 1 and 26")
        if 1 > cardsnum or 26 < cardsnum:
            raise ValueError("invalid value. insert number between 1 and 26")
        if self.was_new_game_called is not True:
            deck = Deckofcards().shuffle_the_pack()
            self.deck = deck
            self.player1.set_hand(cardsnum, self.deck)
            self.player2.set_hand(cardsnum, self.deck)
            self.was_new_game_called = True
        else:
            return "you can not start a new game while the last one is still going"

    def get_winner(self):
        """
        פעולה שבודקת למי יש חבילה גדולה יותר והוא יהיה המנצח
        """
        if len(self.player1.pack) < len(self.player2.pack):
            self.was_new_game_called = self.player1.name
            return self.player1.name
        elif len(self.player1.pack) > len(self.player2.pack):
            self.was_new_game_called = self.player2.name
            return self.player2.name
        elif len(self.player1.pack) == len(self.player2.pack):
            self.was_new_game_called = False
            return "it's a draw"
