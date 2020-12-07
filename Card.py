class Card:

    def __init__(self, value, suitID):
        """
        הגדרת קלף חדש
        הפעולה מוודא שנכניס רק ערכים מתאימים
        אם נכנס ערך שגוי היא תפיל את תתוכנית ותדפיס הערה תואמת
        """
        try:
            if type(value) == int:
                if 1 <= value <= 13:
                    self.value = value
                else:
                    raise ValueError("invalid value! must insert int between 1 and 13")
        except:
            raise ValueError("invalid value! must insert int between 1 and 13")
        try:
            if type(suitID) == str:
                kind = {'diamond': 1, 'spade': 2, 'heart': 3, 'club': 4}
                self.suit = kind[suitID]
        except:
            raise KeyError("invalid value! must insert int right value! \n diamond / spade / heart / club")


    def show(self):
        """
        הפעולה תחזיר יפה תאור של הקלף
        """
        kind = {1: 'diamond', 2: 'spade', 3: 'heart', 4: 'club'}
        return f'the card value is {self.value} \nthe suit is {kind[self.suit]}'

    def __repr__(self):
        """
        הפעולה תחזיר את ערכי הקלף
        """
        kind = {1: 'diamond', 2: 'spade', 3: 'heart', 4: 'club'}
        return f'{self.value, kind[self.suit]}'

    def __eq__(self, other):
        if type(other) != Card:
            return False
        else:
            return self.value == other.value and self.suit == other.suit

    def war(self, *args):
        """
        פעולה שמקבלת מספר קלפים ואומרת מי מהקלפים ינצח
        """
        max_value = self.value
        max_suit = self.suit
        if len(args) > 0:
            for i in args:
                if type(i) is not Card:
                    raise ValueError("The round does'nt count! \n must insert valid value! ")

            for i in range(len(args)):
                if args[i].value == max_value:
                    if args[i].suit > max_suit:
                        max_suit = args[i].suit
                if args[i].value > max_value:
                    if max_value != 1:
                        max_value = args[i].value
                        max_suit = args[i].suit
                if args[i].value < max_value:
                    if args[i].value == 1:
                        max_value = args[i].value
                        max_suit = args[i].suit
            kind = {1: 'diamond', 2: 'spade', 3: 'heart', 4: 'club'}
            c = Card(max_value, kind[max_suit])
            return c
        else:
            raise ValueError("Must insert Card!")
