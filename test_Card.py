from unittest import TestCase
from OurProject.Card import Card

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
        self.assertIsNone(self.c1.war())
        """ 
        גם משווה בין קלפים זהים 
        גם משתמש בערכי קצה
        ומחזיר לי את הקלף המנצח פעם אחת כשהוא זה שמפעיל את הפעולה ופעם אחת כשהוא מופעל בתוך הפעולה
        """
        self.assertTrue(self.c1.war(self.c2, self.c3, self.c4), self.c3)
        self.assertTrue(self.c3.war(self.c1, self.c2, self.c4), self.c3)
        """
        צריך לעשות בדיקה של הזנה של משתנים שונים שאינם קלפים
        """
        # self.assertIsNone(self.c1.war(9,62,7,2,5))
        # self.assertIsNone(self.c1.war('af', 'ga', [14,5,4], ('g'), {1:'ga'}))