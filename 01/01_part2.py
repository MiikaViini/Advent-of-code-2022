file = open("input.txt")
opponent = ''
me = ''
sum = 0

while str:

	str = file.read(4)
	if not str:
		break
	opponent = ord(str[0])
	me = ord(str[2])

	if me == 88:
		if opponent == 65:
			me = 90
		elif opponent == 66:
			me = 88
		elif opponent == 67:
			me = 89
		sum += 0

	elif me == 89:
		if opponent == 65:
			me = 88
		elif opponent == 66:
			me = 89
		elif opponent == 67:
			me = 90
		sum += 3

	elif me == 90:
		if opponent == 65:
			me = 89
		elif opponent == 66:
			me = 90
		elif opponent == 67:
			me = 88
		sum += 6

	if me == 88:
		sum += 1
	elif me == 89:
		sum += 2
	elif me == 90:
		sum += 3
file.close()
print(sum)
