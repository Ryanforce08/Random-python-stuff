from getpass import getpass

play = "Y"

while play.upper() == "Y":
    print("E P I C    R,P,S    B A T T L  E ")
    print()
    print("Select your move (R, P, or S)")
    print()

    player1 = getpass("Player one, what's your choice: ").lower()
    player2 = getpass("Player two, what's your choice: ").lower()
#remove after debug
    #print("Player 1: ", player1)
   # print("Player 2: ", player2)
##########
    if player1 == player2:
        print("It's a tie!")
    elif (player1 == "r" and player2 == "s") or (player1 == "p" and player2 == "r") or (player1 == "s" and player2 == "p"):
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")

    play = input("Play again? (Y or N): ").upper()

print("Thanks for playing!")
