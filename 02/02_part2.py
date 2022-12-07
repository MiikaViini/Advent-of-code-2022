same = 0
i = 0
k = 0
j = 0
sum = 0

with open("input.txt") as file:
	group1 = file.readline()
	group2 = file.readline()
	group3 = file.readline()
	while group1:
		group1 = group1.strip()
		group2 = group2.strip()
		group3 = group3.strip()
		while not same:
			if group1[i] == group2[k]:
				while not same and j < int(len(group3)):
					if group2[k] == group3[j]:
						same = group3[j]
						if same.isupper():
							sum += ord(same) - 38
						elif  same.islower():
							sum += ord(same) - 96
						break
					j += 1
				j = 0

			if i >= int(len(group1)) - 1:
				i = -1
				j = 0
				k += 1
			if k >= int(len(group2)):
				k = 0
				j = 0
				i = -1
				same = ""
				break
			i += 1

		same = ""
		k = 0
		i = 0
		j = 0
		group1 = file.readline()
		group2 = file.readline()
		group3 = file.readline()

print("final", sum)