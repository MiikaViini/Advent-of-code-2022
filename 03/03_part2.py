#!/usr/bin/env python3

total = 0

def	has_same_section(p1_num1, p1_num2, p2_num1, p2_num2):
	if p2_num1 <= p1_num2 and p2_num2 >= p1_num1:
		return True
	else:
		return False

with open("input.txt", "r") as file:
	for line in file:
		pair = line.split(",")
		first = pair[0].split("-")
		second = pair[1].split("-")
		if has_same_section(int(first[0]), int(first[1]), int(second[0]), int(second[1])):
			total += 1

print(total)