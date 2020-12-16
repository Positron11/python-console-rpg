from utilities import *
import time

# map class
class Map():

	def __init__(self, rooms):
		self._rooms = rooms
		self._width = max([room["coordinates"][1][0] for room in rooms.values()])
		self._height = max([room["coordinates"][1][1] for room in rooms.values()])
		self._openings = [opening for room in rooms.values() for opening in room["openings"]]
		self._walls = list()

		# calculate walls
		for room in rooms.values():
			x1 = room["coordinates"][0][0]
			y1 = room["coordinates"][0][1]
			x2 = room["coordinates"][1][0]
			y2 = room["coordinates"][1][1]
			for x in range(x1, x2 + 1):
				for y in range(y1, y2 + 1):
					if (y in [y1,y2] or x in [x1,x2]) and [x,y] not in self._openings:
						self._walls.append([x,y])

	# walls getter
	@property
	def walls(self):
		return self._walls

	# draw map
	def draw(self, player):
		for y in reversed(range(self._height + 1)):
			for x in range(self._width + 1):
				if [x,y] == player.coordinates:
					print("@", end=" ")
				elif [x,y] in self._walls:
					print("#", end=" ")
				else:
					print(".", end=" ")
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

	# moves getter
	@property
	def moves(self):
		return self._moves
		
	# get user input for move
	def get_move(self):
		try:
			move = get_input(f"\n{self.error_message}[move] >> ", self._moves.keys())
			self.error_message = str()
			return move
		except InvalidInputError:
			self.error_message = "<Invalid move!> "
		except BlankInputError:
			self.error_message= "<Empty input!> "


# player class
class Player():

	def __init__(self, name, controller, coordinates=[1,1]):
		self.name = name
		self.coordinates = coordinates
		self._controller = controller

	# change player coordinates
	def move(self, walls):
		move = self._controller.get_move()

		if move:
			# copy and modify current coordinates
			new_coordinates = self.coordinates.copy()
			new_coordinates[self._controller.moves[move][0]] += self._controller.moves[move][1]

			# apply changes if not walking through walls
			if new_coordinates not in walls:
				self.coordinates = new_coordinates
			else: 
				self._controller.error_message = "<Can't go through walls!> "


# game class
class Game():
	
	def __init__(self, map, player):
		self.map = map
		self.player = player

	# play game
	def play(self):
		# title screen
		for i in range(5):
			clear()

			print("WELCOME TO THE GAME")
			print("===================")
			print("\nObjective: navigate")
			print("\nMovement: a,s,d,w")
			print(f"\nStarting in {5 - i}...")
			print("\nBy Aarush Kumbhakern")
			
			time.sleep(1)

		# start game
		while True:
			clear()
			self.map.draw(self.player)
			self.player.move(self.map.walls)