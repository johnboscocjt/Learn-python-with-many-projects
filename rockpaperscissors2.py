import random

options = ("rock", "paper", "scissors")


running = True

# while the game is still running
while running:
    # every time you start the game, reset the game as well as the computer
    player = None
    computer =  random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("Its a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win")
    elif player == "paper" and computer == "rock":
        print("You win")
    elif player == "scissors" and computer == "paper":
        print("You win")
    else:
        print("You lose")
        
    if not input("Play again? (y/n): ").lower() == "y":
        running = False
        
print("Thanks for playing")
