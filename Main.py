from CardGame import CardGame



c = CardGame("Nitzan", "Arad")
print(c.player1.show())
print(c.player2.show())
for i in range(1, 10):
    card1 = c.player1.get_random_card()
    card2 = c.player2.get_random_card()
    if type(card1) == Card and type(card2) == Card:
        if card1.war(card2) == card1:
            c.player1.add_card(card1)
            c.player1.add_card(card2)
            print(f"the winner in this round is {c.player1.name}\n\n")
        else:
            print(f"the winner in this round is {c.player2.name}\n\n")
            c.player2.add_card(card1)
            c.player2.add_card(card2)
    else:
        print("The round does'nt count! \n must insert valid value!")
print(f'the winner of the whole game is {c.get_winner()}')