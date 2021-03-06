from unittest import TestCase
from Card import Card
from Deckofcards import Deckofcards


class TestDeckofcards(TestCase):
    def setUp(self):
        print("setUp")
        self.deck = Deckofcards()

    def tearDown(self):
        print("tearDown")

    def test__str__(self):
        self.assertIn(self.deck.__str__(), f"the package is {self.deck.package}")

    def test_shuffle_the_pack(self):
        self.assertIs(self.deck.shuffle_the_pack(), self.deck.package)

    def test_deal_one(self):
        # בודק האם אני מקבל ערך שהוא קלף
        self.assertIsInstance(self.deck.deal_one(), Card)
        # בודק האם אני מקבל ערך מספרי בערך הקלף
        self.assertIsInstance(self.deck.deal_one().value, int)
        # בודק האם אני מקבל ערך מספרי (מומר ממילה שמייצגת את סוג הקלף) בסוג הקלף
        self.assertIsInstance(self.deck.deal_one().suit, int)
        # בודק אם החבילה ריקה אפשר לשלוף קלף
        deck1 = Deckofcards()
        deck1.package.clear()
        with self.assertRaises(IndexError):
            deck1.deal_one()
        #בודק מה קורה כשאורך החבילה הוא אחד
        deck1 = Deckofcards(2)
        for i in range(3):
            deck1.deal_one()
        t = deck1.package.copy()
        self.assertEqual(deck1.deal_one(), t[0])
        self.assertEqual(len(deck1.package), 0)

    def test_show(self):
        self.assertIn(self.deck.show(), f"the package is {self.deck.package}")


