from unittest import TestCase
from Player import Player
from Deckofcards import Deckofcards

class TestPlayer(TestCase):
    def setUp(self):
        print("setUp")
        self.p1 = Player('arad')

    def tearDown(self):
        print("tearDown")

    def test_show(self):
        self.assertIn(self.p1.show(),  f'{self.p1.name} have the package {self.p1.pack}')

    def test_set_hand(self):
        self.assertIsNone(self.p1.set_hand(self.p1.pack, 0))
        self.assertIsNone(self.p1.set_hand(self.p1.pack, 53))
        self.assertIsNone(self.p1.set_hand((1,3), 4))
        self.assertIsNone(self.p1.set_hand([3,4,5], 'ty'))
        # מחזיר שגיאה אבל שיחזיר שגיאה גם בגלל שהכנסתי רשימה לא של קלפים
        self.assertIsNone(self.p1.set_hand([1,56,6], 6))
        # למה אני לא מקבל חבילה?
        deck = Deckofcards()
        self.assertIs(self.p1.set_hand(deck,10), self.p1.pack)


    def test_get_random_card(self):
        pass

    def test_add_card(self):
        pass