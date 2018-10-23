'''
All of my favorite custom functions!
Currently contains numInput, stringInput, reverse, aesthetic, and wordCount.
All functions are documented.
'''


def numInput(message, error="Incorrect input. Try again."): 
	'''
	For asking the user for a number input.
	If the input is not a number, prints "Incorrect input. Try again" or your custom error message and reprints the question.
	Takes one required argument, which is the message to print.
	Takes one optional argument next, which is the error message.
	Both arguments must be strings.
	'''
	while True:
		try:
			num = int(input(message))
			return num
		except ValueError:
			print(error)
			

def reverse(word):
	'''
	Takes a string, and returns it backwards.
	'''
	list = []
	for i in word:
		list.append(i)
	list.reverse()
	list = ''.join(list)
	return list
	

def wordCount(word):
	'''
	Returns the amount of words (seperated by spaces) in a string.
	'''
	return len(word.split())
	

def stringInput(message, error="Incorrect input. Try again."):
	'''
	Asks the user for a word input.
	If input is not compatible with strings, prints "Incorrect input. Try again." (or your custom error message) and reprints the question.
	Takes one required argument, which is the message to print.
	Takes one optional argument next, which is the error message.
	Both arguments must be strings.
	'''
	while True:
		try:
			word = str(input(message))
			return word
		except ValueError:
			print(error)

	
def aesthetic(string):
	'''
	a e s t h e t i c
	'''
	nstring = ''
	for s in string:
		ns = s + ' '
		nstring = nstring + ns
	return nstring
			
if __name__ ==  '__main__':
	print('Why would you run this?')
