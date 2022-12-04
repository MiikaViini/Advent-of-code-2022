file = open("input.txt")
top_cals = 0
sec_cals = 0
third_cals = 0
char = '1'
end = 0

# Loop through input file and break when reached end of file
while char:

	char = ''
	change_elv = 0
	str = ""
	cur_cals = 0

	while change_elv != 1:
		while not '\n' in char:
			str += char
			char = file.read(1)
			if not char:
				end = 1
				break
		if end == 1:
			break
		cur_cals += int(str, 10)
		str = ""

		if '\n' in char:
			char = file.read(1)
			if '\n' in char:
				change_elv = 1

# Evaluate calories
	if cur_cals > top_cals:
		third_cals = sec_cals
		sec_cals = top_cals
		top_cals = cur_cals
	elif cur_cals > sec_cals and cur_cals != top_cals:
		third_cals = sec_cals
		sec_cals = cur_cals
	elif cur_cals > third_cals and cur_cals != sec_cals:
		third_cals = cur_cals
	if end == 1:
		break
	
file.close()
print("highes amount of calories carried by on elv", top_cals)
print("highes amount of calories carried by on elv", sec_cals)
print("highes amount of calories carried by on elv", third_cals)
print("all together", top_cals + sec_cals + third_cals)
