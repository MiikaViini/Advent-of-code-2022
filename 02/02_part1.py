same = ""
i = 0
k = 0
sum = 0

with open("input.txt") as file:
	str = file.readline()

	while str:
		str = str.strip()
		rucksack_len = len(str) / 2
		rucksack1 = str[0:int(rucksack_len)]
		rucksack2 = str[int(rucksack_len) : int(rucksack_len) * 2]

		while not same:
			if rucksack1[i] == rucksack2[k]:
				same = rucksack1[i]
				break

			elif i >= int(rucksack_len) - 1:
				i = -1
				k += 1
			i += 1

		if same.isupper():
			sum += ord(same) - 38
		
		elif  same.islower():
			sum += ord(same) - 96


		same = ""
		k = 0
		i = 0
		str = file.readline()

print("final", sum)