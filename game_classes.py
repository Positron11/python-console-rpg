from utilities import *
import time

# map class
class Map():

	def __init__(self, rooms):
		self._rooms = rooms
		self._width = max([room["coordinates"][1][0] for room in rooms.values()])
		self._height = max([room["coordinates"][1][1] for room in rooms.values()])
		self._openings = [opening for room in rooms.values() for opening in room["openings"]]
		self._room_coordinates = dict()
		self._walls = list()

		# calculate walls and room coordinates
		for room in rooms.values():
			x1 = room["coordinates"][0][0]
			y1 = room["coordinates"][0][1]
			x2 = room["coordinates"][1][0]
			y2 = room["coordinates"][1][1]
			self._room_coordinates.update({room["name"]: list()})

			for x in range(x1, x2 + 1):
				for y in range(y1, y2 + 1):
					self._room_coordinates[room["name"]].append([x,y])
					if (y in [y1,y2] or x in [x1,x2]) and [x,y] not in self._openings:
						self._walls.append([x,y])

	# walls getter
	@property
	def walls(self):
		return self._walls

	# get room user is currently in
	def current_room(self, player):
		for room, coordinates in self._room_coordinates.items():
			if player.coordinates in coordinates:
				return room

	# draw map
	def draw(self, player):
		for y in reversed(range(self._height + 1)):
			for x in range(self._width + 1):
				if [x,y] == player.coordinates:
					print(f"{colorify(player.sprite, 'red', 'bold')}", end=" ")
				elif [x,y] in self._walls:
					print(f"{colorify('#', 'grey')}", end=" ")
				else:
					print(f"{colorify('.', 'green', 'bold')}", end=" ")
			print()


# controller class
class Controller():
	# keymappings
	_moves = {
		"a": [0, -1],
		"s": [1, -1],
		"d": [0, 1],
		"w": [1, 1]
	}

	def __init__(self):
		self.error_message = str()
		self.status_line = "Start game..."

	# moves getter
	@property
	def moves(self):
		return self._moves

	# construct colored prompts
	def colored_prompt(self, prompt, error):
		return f"\n{colorify(f'<{self.error_message}>', 'red', 'bold') if self.error_message else colorify(f'({self.status_line})', 'green', 'bold')} [{prompt}] >> "

	# take input and handle common error messages
	def errored_input(self, **kwargs):
		try:
			value = get_input(kwargs.get("prompt"), kwargs.get("valid"), kwargs.get("max_length", 250), kwargs.get("invert", False))
			self.error_message = str()
			return value
		except InvalidInputError:
			self.error_message = f"Invalid {kwargs.get('object')}!"
		except ExceededMaxLengthError:
			self.error_message = f"Too long! Max length: {kwargs.get('max_length')} characters"
		except BlankInputError:
			self.error_message= "Empty input!"

	# set sprite
	def set_sprite(self):
		return self.errored_input(prompt=self.colored_prompt("choose sprite", self.error_message), valid=["#", "."], max_length=1, invert=True, object="sprite")

	# get user input for move
	def get_move(self):
		return self.errored_input(prompt=self.colored_prompt("move", self.error_message), valid=self._moves.keys(), object="move")


# player class
class Player():

	def __init__(self, controller, sprite="X", coordinates=[1,1]):
		self.sprite = sprite
		self.coordinates = coordinates
		self._controller = controller

	# set player sprite
	def change_sprite(self):
		self.sprite = self._controller.set_sprite()

	# change player coordinates
	def move(self, map):
		move = self._controller.get_move()

		if move:
			# copy and modify current coordinates
			new_coordinates = self.coordinates.copy()
			new_coordinates[self._controller.moves[move][0]] += self._controller.moves[move][1]

			# apply changes if not walking through walls
			if new_coordinates not in map.walls:
				self.coordinates = new_coordinates
				self._controller.status_line = f"You're in the {map.current_room(self)}"
			else: 
				self._controller.error_message = "Can't go through walls!"


# game class
class Game():
	
	def __init__(self, map, player):
		self.map = map
		self.player = player

	# play game
	def play(self):
		# title screen
		while True:
			clear()
			print("WELCOME TO THE GAME")
			print("===================")
			print("\nObjective: navigate")
			print("\nMovement: a,s,d,w")

			# choose sprite
			self.player.change_sprite()
			if not self.player._controller.error_message:
				break

		# start game
		while True:
			clear()
			self.map.draw(self.player)
			self.player.move(self.map)