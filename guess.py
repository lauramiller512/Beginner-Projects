from random import randint
num = randint(1,100)

guessesTaken = 0

while guessesTaken < 7:
	guess = int(input("Guess a number: "))
	guessesTaken = guessesTaken + 1

	if guess < num:
		print("Too low, guess again")
	if guess > num:
		print("Too high, guess again")
	if guess == num:
		print("Holy shit, you got it!")
		break

if guess != num:
	print(f"Sorry, the number I was thinking of was {num}.")