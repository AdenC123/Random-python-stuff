import random
import sys
	
def numInput(message):
	#function for safely inputting a number
	while True:
		try:
			num = int(input(message))
			return num
		except ValueError:
			print("That's not a number! Try again.")

def main():
	
	#define variables
	odds = numInput("Welcome to Guess The Number! The computer will pick a number between 1 and: ")
	randNum = random.randint(1, odds)
	userNum = numInput("Now pick your number between 1 and {}!".format(odds))
	tries = 1
	
	#main game
	while randNum != userNum:
		if userNum > randNum:
			userNum = numInput("Too high! Enter another number: ")
		elif userNum < randNum:
			userNum = numInput("Too low! Enter another number:  ")
		tries += 1
	
	#win condition
	print("YOU WIN! It took you {} tries to guess the number!".format(tries))
	name = input("Enter your name for the leaderboard: ")
	
	#update highscore list
	with open('guessthenumber_highscores.txt', 'a') as highscore:
		highscore.write('{} guessed the number {} in {} tries with the odds of {}!\n'.format(name, randNum, tries, odds))
		print('Recorded!')
	
	#check/clear highscore list
	while True:
		yn = input('Would you like to see the highscores? (y/n)')
		if yn == 'y':
			print('\n')
			with open('guessthenumber_highscores.txt', 'r') as highscore:
				for line in highscore:
					print(line)
			print('\n')
			clear = input('Would you like to clear highscores? If yes, type "clear". If no, press enter.')
			if clear == 'clear':
				clear2 = input('Are you sure? This cannot be undone! Type "clear" if yes, press enter if no.')
				if clear2 == 'clear':
					f = open('guessthenumber_highscores.txt', 'r+')
					f.truncate()
					f.close()
					print('Cleared.')
			break
		elif yn == 'n':
			break
		else: 
			print('Please input y or n.')
	
	#ask to play again
	while True:	
		yn = input('Would you like to play again? (y/n)')
		if yn == 'y':
			print('\n')
			break
		elif yn == 'n':
			print("Goodbye!")
			sys.exit()
		else:
			print('Please input y or n.')
			
if __name__ == '__main__':
	while True:
		main()
