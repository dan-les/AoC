#!/usr/bin/env python3
# --- Day 2: Password Philosophy ---
# https://adventofcode.com/2020/day/2
# Daniel Lesniewicz, 250996

def main():

	# czesc I
	# po odseparowaniu wlasciwych danych w IF'ie sprawdzam czy dany znak wystepuje 
	# odpowiednia ilosc razy (w przedziale <minQuantity, maxQuantity>)

	counter1 = 0 # zmienna przechowywujaca ilosc poprawnych hasel

	with open("inputDay2.txt") as file:
		for line in file:
			minQuantity, maxQuantity, letter, password = separate(line)
			quantity = password.count(letter)
			if(minQuantity <= quantity and quantity <= maxQuantity):
				counter1 += 1

	print("Part I:  ", counter1)

	# czesc II
	# po odseparowaniu wlasciwych danych w IF'ie sprawdzam czy dany znak wystepuje 
	# na jednej z pozycji (position1 lub position2), ale nie na obu jednoczesnie 

	counter2 = 0 # zmienna przechowywujaca ilosc poprawnych hasel

	with open("inputDay2.txt") as file:
		for line in file:
			position1, position2, letter, password = separate(line)
			quantity = password.count(letter)
			if((letter == password[position1 - 1] ) != (letter == password[position2 - 1])):
				counter2 += 1

	print("Part II: ", counter2)


def separate(line):
    details, password = line.split(': ', 1)
    rangeNumbers, letter = details.split()
    number1, number2 = map(int, rangeNumbers.split('-'))

    return number1, number2, letter, password


if __name__ == '__main__':
    main()