import os
import re
from collections import Counter

with open(os.path.join(os.path.dirname(__file__), 'data/day4.txt')) as input:
    word_search = input.read().splitlines()
    word_count = Counter()

    for row in range(0, len(word_search)):
        for column in range(0, len(word_search[0])):
            if column < len(word_search[0]) - 3:
                word_count.update([''.join([word_search[row][column], word_search[row][column + 1], word_search[row][column + 2], word_search[row][column + 3]])])

            if row < len(word_search) - 3:
                word_count.update([''.join([word_search[row][column], word_search[row + 1][column], word_search[row + 2][column], word_search[row + 3][column]])])

                if column < len(word_search[0]) - 3:
                    word_count.update([''.join([word_search[row][column], word_search[row + 1][column + 1], word_search[row + 2][column + 2], word_search[row + 3][column + 3]])])

                if column > 2:
                    word_count.update([''.join([word_search[row][column], word_search[row + 1][column - 1], word_search[row + 2][column - 2], word_search[row + 3][column - 3]])])

    print("Part 1:", word_count.get("XMAS") + word_count.get("SAMX"))

    valid_starting_points = []

    for row in range(1, len(word_search) - 1):
        for column in range(1, len(word_search[0]) - 1):
            if word_search[row][column] == "A":
                valid_starting_points.append((row, column))

    def is_valid_xmass(row, column):
        lhs = ''.join([word_search[row - 1][column - 1], word_search[row][column], word_search[row + 1][column + 1]])
        rhs = ''.join([word_search[row - 1][column + 1], word_search[row][column], word_search[row + 1][column - 1]])
        return (lhs == "MAS" or lhs == "SAM") and (rhs == "MAS" or rhs == "SAM")

    xmasses = filter(lambda coords: is_valid_xmass(coords[0], coords[1]), valid_starting_points)

    print("Part 2:", len(list(xmasses)))

