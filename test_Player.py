from unittest import TestCase
from Player import Player
from Card import Card
from CardGame import CardGame


class TestPlayer(TestCase):
    def setUp(self):
        print("setUp")
        self.p1 = Player('arad')
        self.c = CardGame('arad', 'nitzan')

    def tearDown(self):
        print("tearDown")

    def test_show(self):
        # מדפיס יפה את הערכים
        self.assertIn(self.p1.show(), f'{self.p1.name} have the package {self.p1.pack}')

    def test_set_hand(self):
        # בודק ערך מחוץ לתחום
        with self.assertRaises(IndexError):
            self.p1.set_hand(0, self.p1.pack)
        with self.assertRaises(IndexError):
            self.p1.set_hand(53, self.p1.pack)
        # מקבל ערך שהוא לא מספר עבור מספר קלפים
        with self.assertRaises(TypeError):
            self.p1.set_hand((1, 3), self.p1.pack)
        with self.assertRaises(TypeError):
            self.p1.set_hand('ty', [3, 4, 5])
        # לא מקבל רשימה בתור חבילת קלפים
        with self.assertRaises(TypeError):
            self.p1.set_hand(6, 2)

    def test_get_random_card(self):
        # בודק האם אני מקבל ערך מסוג קלף
        self.assertIsInstance(self.c.player2.get_random_card(), Card)
        # האם אפשר למשוך קלף מחבילה ריקה
        with self.assertRaises(IndexError):
            self.p1.pack.clear()
            self.p1.get_random_card()
        c = CardGame('arad', 'nitzan', 1)
        t = c.player1.pack.copy()
        self.assertEqual(c.player1.get_random_card(), t[0])

    def test_add_card(self):
        # בודק מה קורה אם לא הכנסנו ערך לפעולה בכלל
        with self.assertRaises(ValueError):
            self.p1.add_card()
        # בודק מה קורה אם הכנסנו ערך לא נכון לפעולה
        with self.assertRaises(TypeError):
            self.p1.add_card(2)
        c1 = Card(4, 'club')
        self.p1.add_card(c1)
        self.assertIn(c1, self.p1.pack)
