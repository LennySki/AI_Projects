position = [0,0]

movements = {

	'up': (-1, 0),
	'down': (1, 0),
	'left': (0, -1),
	'right': (0, 1)
}

commands = ['right', 'right', 'down', 'down', 'down', 'left']

for command in commands:
	move = movements[command]
	position[0] += move [0]
	position[1] += move[1]
	print(f"Moved {command}: New Position = {position}")

print("Final position:", position)
