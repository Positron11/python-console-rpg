from game_classes import *

# define rooms
rooms = {
	"hall": {"name": "living room", "coordinates": [[5,0], [10,7]], "openings": [[5,5], [5,6], [6,7]]},
	"dining": {"name": "dining room", "coordinates": [[0,4], [5,7]], "openings": [[5,5], [5,6], [3,4], [4,4]]},
	"kitchen": {"name": "kitchen", "coordinates": [[0,0], [5,4]], "openings": [[3,4], [4,4]]},
	"hallway": {"name": "hallway", "coordinates": [[5,7], [7,10]], "openings": [[6,7], [6,10], [7,8], [5,9]]},
	"mbathroom": {"name": "master bathroom", "coordinates": [[0,7], [3,10]], "openings": [[3,8]]},
	"mbedroom": {"name": "master bedroom", "coordinates": [[0,7], [5,15]], "openings": [[5,9]]},
	"cbedroom": {"name": "child bedroom", "coordinates": [[5,10], [10,15]], "openings": [[6,6]]},
	"cbathroom": {"name": "common bathroom", "coordinates": [[7,7], [10,10]], "openings": [[7,8]]}
}

# create entities
map = Map(rooms)
controller = Controller()
player = Player(controller)
game = Game(map, player)

# play game
game.play()