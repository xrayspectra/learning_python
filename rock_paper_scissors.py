player_1 = input("Enter your choice, player_1: ")
print("NO CHEATING\n" * 20)
player_2 = input("Enter your choice, player_2: ")

if player_1 == player_2:
    print("It's a win-win!")

elif player_1 == "rock":
    if player_2 == "paper":
        print ("Player 2 wins!")
    elif player_2 == "scissors":
        print("Player 1 wins!")

elif player_1 == "paper":
    if player_2 == "scissors":
        print ("Player 2 wins!")
    elif player_2 == "rock":
        print("Player 1 wins!")

elif player_1 == "scissors":
    if player_2 == "rock":
        print ("Player 2 wins!")
    elif player_2 == "paper":
        print("Player 1 wins!")
else:
    print ('Players, please, check your input!')