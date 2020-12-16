from os import system, name 
from custom_exceptions import *

# colors
colors = {
	"endc": "\033[0m",
	"bold": "\033[1m",
	"red": "\033[0;31m",
	"blue": "\033[0;34m",
	"grey": "\033[0;37m",
	"green": "\033[0;32m"
}

  
# clear function 
def clear(): 
	# for windows 
	if name == 'nt': 
		_ = system('cls') 
  
	# for mac and linux (posix)
	else: 
		_ = system('clear') 


# get input function
def get_input(prompt, valid, max_length=250, invert=False):
	# get input
	user_input = input(prompt)

	# if any input at all
	if user_input:
		# either return input or exception
		if (user_input not in valid) is not invert:
			raise InvalidInputError()
		elif len(user_input) > max_length:
			raise ExceededMaxLengthError()
		else:
			return user_input
	else:
		raise BlankInputError()


# color fuction
def colorify(string, color, style=None):
	return f"{colors[color]}{colors[style] if style else ''}{string}{colors['endc']}"