#18-21 wristband
#21+ drink, normal entry
#too young, sorry
try:
	age = int(input("Hold old are you: ")) 	#turns input into an integer
except ValueError:		#returns error if not a number specifically
	print("That's not a number...")
	exit()
if age >= 18:
	print("You can enter but need a wristband.")
elif age >= 21:
	print("You're good to go - don't drink too much!")
elif age < 18:
	print("Sorry but you're too young.")