from random import randint

# 1. Set odds 2. Choose number between 1 and odds 3. ask for number 4. compare user number and random number

def numInput(message): 
	while True:
		try:
			num = int(input(message))
			return num
			break		
		except ValueError:
			print("That's not a number! Try again.")
		
odds = numInput("Welcome to the Python Number Guesser 2000! Pick your odds! Your odds will be between 1 and: ")

randNum = randint(1, odds)
userNum = numInput("Pick an number between 1 and %d: " % odds)

if userNum == randNum:
	print('YOU WIN!')
else:
	print("The number was %d! Try again..." % randNum)
