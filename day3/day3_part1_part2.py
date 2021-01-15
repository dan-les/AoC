#!/usr/bin/env python3
# --- Day 3: Toboggan Trajectory ---
# https://adventofcode.com/2020/day/3
# Daniel Lesniewicz, 250996

# wczytanie z pliku
with open('inputDay3.txt') as file:
    treeBoard = [line.rstrip() for line in file]


def main():
    # czesc I
    result1 = countTrees(3, 1)
    print("Part  I:", result1)

    # czesc II
    result2_1 = countTrees(1, 1)
    result2_2 = result1
    result2_3 = countTrees(5, 1)
    result2_4 = countTrees(7, 1)
    result2_5 = countTrees(1, 2)

    result2 = result2_1 * result2_2 * result2_3 * result2_4 * result2_5
    print("Part II:", result2)


def countTrees(moveX, moveY):
    counter = 0
    currentPositionX = 0
    currentPositionY = 0

    treeBoardHeight = len(treeBoard)
    treeBoardWidth = len(treeBoard[0])

    # przeszukiwanie drzewa
    while currentPositionY < treeBoardHeight: #dopóki nie doszliśmy do końca w pionie (płaszczyzna Y)

        # jesli wyszlismy w poziomie za dostepna plansze
        if currentPositionX > treeBoardWidth - 1:
            # to cofamy sie o szerokosc planszy do analogicznego punktu
            currentPositionX -= treeBoardWidth

        # jesli napotakmy drzewo to zwiekszamy licznik
        if treeBoard[currentPositionY][currentPositionX] == '#':
            counter += 1

        # przesuniecie sie w prawo i w dol
        currentPositionX += moveX
        currentPositionY += moveY

    return counter


if __name__ == '__main__':
    main()
