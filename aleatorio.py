import random
def pick_winner():
	lines = []
	with open("list.txt", "r") as f:
		lines = f.readlines();
	num = random.randrange(0, len(lines))
	print lines[num]

pick_winner()