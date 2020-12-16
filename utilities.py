from os import system, name 
from custom_exceptions import *
  
# clear function 
def clear(): 
	# for windows 
	if name == 'nt': 
		_ = system('cls') 
  
	# for mac and linux (posix)
	else: 
		_ = system('clear') 


# get input function
def get_input(prompt, valid, invert=False):
	# get input
	user_input = input(prompt)

	# if any input at all
	if user_input:
		# either return input or exception
		if (user_input not in valid) is not invert:
			raise InvalidInputError()
		else:
			return user_input
	else:
		raise BlankInputError()