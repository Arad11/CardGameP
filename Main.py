from Card import Card
from Player import Player
import random
from Deckofcards import Deckofcards
from CardGame import CardGame

#החדש
c = CardGame("Nitzan", "Arad")
print(c.player1.show())
print(c.player2.show())
for i in range(1, 10):
    first = c.player1.get_random_card()
    second = c.player2.get_random_card()
    val1 = list(first.items())[0][0]
    suit1 = list(first.items())[0][1]
    card1 = Card(val1, suit1)
    val2 = list(second.items())[0][0]
    suit2 = list(second.items())[0][1]
    card2 = Card(val2, suit2)
    kind = {'diamond': 1, 'spade': 2, 'heart': 3, 'club': 4}
    if card1.war(card2) == card1:
        c.player1.add_card(card1)
        c.player1.add_card(card2)
        print(f"the winner in this round is {c.player1.name}\n\n")
    else:
        print(f"the winner in this round is {c.player2.name}\n\n")
        c.player2.add_card(card1)
        c.player2.add_card(card2)

print(f'the winner of the whole game is {c.get_winner()}')



# cplayer=0
# c = CardGame("Nitzan", "Arad")
# print(c.player1.show())
# print(c.player2.show())
# for i in range(1, 10):
#     first = c.player1.get_random_card()
#     second = c.player2.get_random_card()
#     val1 = list(first.items())[0][0]
#     suit1 = list(first.items())[0][1]
#     card1 = Card(val1, suit1)
#     val2 = list(second.items())[0][0]
#     suit2 = list(second.items())[0][1]
#     card2 = Card(val2, suit2)
#     kind = {'diamond': 1, 'spade': 2, 'heart': 3, 'club': 4}
#     if card1.war(card2) == card1:
#         cplayer += 1
#         c.player1.add_card(card1)
#         c.player1.add_card(card2)
#         print(f"the winner in this round is {c.player1.name}\n\n")
#     else:
#         print(f"the winner in this round is {c.player2.name}\n\n")
#         c.player2.add_card(card1)
#         c.player2.add_card(card2)
#
# if cplayer > 5:
#     print(f'{c.player1.name} is the winner')
# elif cplayer < 5:
#     print(f'{c.player2.name} is the winner')
# else:
#     print("even")
#
