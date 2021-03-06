# custom exception for invalid input
class InvalidInputError(Exception):
	pass

# custom exception for blank input
class BlankInputError(Exception):
	pass

# custom exception for exceeding max length
class ExceededMaxLengthError(Exception):
	pass