#!/usr/bin/env python3
# --- Day 1: Report Repair ---
# https://adventofcode.com/2020/day/1
# Daniel Lesniewicz, 250996


def main():

	with open("inputDay1.txt") as file:
		lines = file.readlines()
		lines = [int(x.strip()) for x in lines] 

	# czesc I
	# sprawdzanie warunku poprzez przejrzenie wszystkich kombinacji oraz nastepnie obliczenie iloczynu
	size = len(lines)
	for i in range (0, size):
		for j in range (i + 1, size):
			sum = lines[i] + lines[j]
			if sum == 2020:	
				print("( number1, number2 ): (", lines[i],", ",lines[j],")")
				# wynik to iloczyn 2 liczb
				result = lines[i] * lines[j]

	print("Part  I:", result, "\n")

	# czesc II
	# sprawdzanie warunku poprzez przejrzenie wszystkich kombinacji oraz nastepnie obliczenie iloczynu
	for i in range (0, size):
		for j in range (i + 1, size):
			for k in range (j +1, size):
				sum = lines[i] + lines[j] + lines[k]
				if sum == 2020:	
					print("( number1, number2, number3 ): (", lines[i],", ",lines[j],", ",lines[k],")")
					# wynik to iloczyn 3 liczb
					result = lines[i] * lines[j] * lines[k]
				
	print("Part  II:", result, "\n")

if __name__ == '__main__':
    main()