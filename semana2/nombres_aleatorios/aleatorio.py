import random
def pick_winner():
	lines = []
	with open("nombres.txt", "r") as f:
		lines = f.readlines();
	num = random.randrange(0, len(lines))
	print lines[num]

pick_winner()