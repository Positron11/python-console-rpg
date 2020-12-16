from game_classes import *

# define rooms
rooms = {
	"hall": {"coordinates": [[5,0], [10,7]], "openings": [[5,5], [5,6], [6,7]]},
	"dining": {"coordinates": [[0,4], [5,7]], "openings": [[5,5], [5,6], [3,4], [4,4]]},
	"kitchen": {"coordinates": [[0,0], [5,4]], "openings": [[3,4], [4,4]]},
	"hallway": {"coordinates": [[5,7], [7,10]], "openings": [[6,7], [6,10], [7,8], [5,9]]},
	"mbedroom": {"coordinates": [[0,7], [5,15]], "openings": [[5,9]]},
	"mbathroom": {"coordinates": [[0,7], [3,10]], "openings": [[3,8]]},
	"cbedroom": {"coordinates": [[5,10], [10,15]], "openings": [[6,6]]},
	"cbathroom": {"coordinates": [[7,7], [10,10]], "openings": [[7,8]]}
}

# create entities
map = Map(rooms)
controller = Controller()
player = Player(controller)
game = Game(map, player)

# play game
game.play()