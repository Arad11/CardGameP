from unittest import TestCase
from CardGame import CardGame


class TestCardGame(TestCase):
    def setUp(self):
        print("setUp")
        self.c1 = CardGame("Arad", 'Nitzan')

    def tearDown(self):
        print("tearDown")

    def test__str__(self):
        self.assertIn(self.c1.__str__(), f'player1 {self.c1.player1} \n player2 {self.c1.player2}')

    def test_new_game(self):
        self.assertIn(self.c1.new_game(), "you can not start a new game while the last one is still going")
        with self.assertRaises(ValueError):
            self.c1.new_game('ah')
        with self.assertRaises(ValueError):
            self.c1.new_game((1, 2))
        with self.assertRaises(ValueError):
            self.c1.new_game(45)

    def test_get_winner(self):
        self.c1.player2.pack.clear()
        self.assertTrue(self.c1.get_winner(), self.c1.player2)
        self.c1.player1.pack.clear()
        self.assertIn(self.c1.get_winner(), "it's a draw")
