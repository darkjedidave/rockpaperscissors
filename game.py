from random import randint
# # rock, paper, scissors game
# # Simple AI version

player_wins = 0
computer_wins = 0
winning_score = 5
#game currently set to first player to win 5 rounds wins the game

while player_wins < winning_score and computer_wins < winning_score:
    print(f"Player Score: {player_wins} Computer Score: {computer_wins}")
    print("Rock...")
    print("Paper...")
    print("Scissors...")

    player = input("(Enter your choice): ").lower()
    if player == "quit" or player =="q":
        break
    rand_num = randint(0, 2)
    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"
    else:
        computer = "scissors"
    print(f"computer plays {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock":
        if computer == "scissors":
            print("player wins!")
            player_wins += 1
        else:
            print("computer wins!")
            computer_wins += 1
    elif player == "paper":
        if computer == "rock":
            print("player wins!")
            player_wins += 1
        else:
            print("computer wins!")
            computer_wins += 1
    elif player == "scissors":
        if computer == "paper":
            print("player wins!")
            player_wins += 1
        else:
            print("computer wins!")
            computer_wins += 1
    else:
        print("Please enter a valid move!")

if player_wins > computer_wins:
    print("CONGRATS, YOU WON!")
elif player_wins == computer_wins:
    print("IT'S A TIE...")
else:
    print("OH NO :( COMPUTER WON")
print(f"FINAL SCORES... Player: {player_wins} Computer: {computer_wins}")





