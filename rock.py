from random import randint

player = input("Player, make your guess: ").lower()
comp_guess = randint(0,2)

if comp_guess == 0:
	computer = "rock"
elif comp_guess == 1:
	computer = "paper"
else:
	computer = "scissors"

print(f"Computer plays {computer}")

if player == computer:
	print("That's a tie!")
elif player == "rock":
	if computer == "scissors":
		print("You win")
	else:
		print("Computer wins")
elif player == "paper":
	if computer == "rock":
		print("You win")
	else:
		print("Computer wins")
elif player == "scissors":
	if computer == "paper":
		print("You win")
	else:
		print("Computer wins")
else:
	print("Please enter a valid move")