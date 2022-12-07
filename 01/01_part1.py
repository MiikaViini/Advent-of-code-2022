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

	if (opponent == 65 and me == 90) or \
		(opponent == 66 and me == 88) or (opponent == 67 and me == 89):
		sum += 0
	elif (opponent == 65 and me == 88) or \
		 (opponent == 66 and me == 89) or (opponent == 67 and me == 90):
		sum += 3
	elif (opponent == 65 and me == 89) or \
		(opponent == 66 and me == 90) or (opponent == 67 and me == 88):
		sum += 6

	if me == 88:
		sum += 1
	elif me == 89:
		sum += 2
	elif me == 90:
		sum += 3
file.close()
print(sum)