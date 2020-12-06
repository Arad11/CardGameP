class Card:
    # הישן
    # def __init__(self, value, suitID):
    #     """
    #     פעולה שמגדירה קלף ומאמתת שמקבל רק נתונים הגיוניים
    #     """
    #     if isinstance(value, str):
    #         if value.isnumeric():
    #             if 1 <= int(value) <= 13:
    #                 self.value = value
    #             else:
    #                 raise ValueError("invalid value! \n value must be number between 1 and 13")
    #         else:
    #             raise ValueError("invalid value! \n value must be number between 1 and 13")
    #     elif not isinstance(value, int):
    #         raise ValueError("invalid value! \n value must be number between 1 and 13")
    #     elif value < 1 or value > 13:
    #         raise ValueError("invalid value! \n value must be number between 1 and 13")
    #     else:
    #         self.value = value
    #     kind = {'diamond': 1, 'spade': 2, 'heart': 3, 'club': 4}
    #
    #     try:
    #         self.suit = kind[suitID]
    #     except:
    #         raise KeyError("invalid key! \n key must be diamond \ spade \ heart \ club")


    # החדש
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
        return f'{self.value, self.suit}'

    def __eq__(self, other):
        if type(other) != Card:
            return False
        return self.value == other.value and self.suit == other.suit

    def war(self, *args):
        """
        פעולה שמקבלת מספר קלפים ואומרת מי מהקלפים ינצח
        חסר לוודא שאני מקבל רק קלפים ולא משתנים מסוגים אחרים
        """
        max_value = self.value
        max_suit = self.suit
        if len(args) > 0:
            for i in args:
                if type(i) is not Card:
                    print("The round does'nt count! \n must insert valid value! ")
                    return None

            for i in range(len(args)):
                if args[i].value == max_value:
                    if args[i].suit < max_suit:
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
            print("The round does'nt count! \n must insert valid value! ")
            return None
