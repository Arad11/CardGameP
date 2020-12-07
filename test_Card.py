from unittest import TestCase
from Card import Card


class TestCard(TestCase):
    def setUp(self):
        print("setUp")
        self.c1 = Card(13, "heart")
        self.c2 = Card(6, "club")
        self.c3 = Card(1, "diamond")
        self.c4 = Card(1, "club")

    def tearDown(self):
        print("tearDown")

    def test_show(self):
        """
        בודק שמודפס הקלף
        """
        self.assertIn(self.c1.show(), f'the card value is 13 \nthe suit is heart')

    def test_war(self):
        """
        בודק האם אני מקבל None כשאני לא מכניס כלום לפונקציה
        """
        with self.assertRaises(ValueError):
            self.c3.war()
        """ 
        גם משווה בין קלפים עם ערכים זהים 
        גם משתמש בערכי קצה
        ומחזיר לי את הקלף המנצח פעם אחת כשהוא זה שמפעיל את הפעולה ופעם אחת כשהוא מופעל בתוך הפעולה
        """
        self.assertEqual(self.c1.war(self.c2, self.c3, self.c4), self.c4)
        self.assertEqual(self.c4.war(self.c1, self.c2, self.c3), self.c4)
       # """ הזנה של משתנים שונים שאינם קלפים"""
        with self.assertRaises(ValueError):
            self.c3.war(4)
        with self.assertRaises(ValueError):
            self.c3.war({4: 'ga'})
        with self.assertRaises(ValueError):
            self.c3.war(('ah',4))
        with self.assertRaises(ValueError):
            self.c3.war('ah')

    def test__init__(self):
        """
        בודק האם ניתן להגדיר קלף לא בתחום או אם סוג לא קיים
        """
        with self.assertRaises(ValueError):
            card10 = Card(14, 'heart')
        with self.assertRaises(KeyError):
            card10 = Card(6, 'sh')































