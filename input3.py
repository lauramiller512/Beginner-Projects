from random import randint
num = randint(1, 1000)

if int(num)%2 == 0:	#The operator % called modulus checks for the remainder
	print("even")
else:
	print("odd")		#Test comment
