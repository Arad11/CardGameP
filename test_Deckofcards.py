from unittest import TestCase
from OurProject.Card import Card
from OurProject.Deckofcards import Deckofcards

class TestDeckofcards(TestCase):
    def setUp(self):
        print("setUp")
        self.deck = Deckofcards()

    def tearDown(self):
        print("tearDown")

    def test_shuffle_the_pack(self):
        self.assertIs(self.deck.shuffle_the_pack(), self.deck.package)

    def test_deal_one(self):
        self.assertIsInstance(self.deck.deal_one(), tuple)
        self.assertEqual(len(self.deck.deal_one()), 2)
        """חחחחחחחחחחחחחחחחחחחחחחחחחחחחח מה???"""
        # self.assertIsInstance(type(self.deck.deal_one()[0]), int)

    def test_show(self):
        self.assertIn(self.deck.show(), f"the package is {self.deck.package}")


