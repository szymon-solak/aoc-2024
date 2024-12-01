import os
import re

with open(os.path.join(os.path.dirname(__file__), 'data/day1.txt')) as input:
    pairs = [re.split(r"\s+", line) for line in input.read().splitlines()]
    lhs = sorted(map(lambda pair: int(pair[0]), pairs))
    rhs = sorted(map(lambda pair: int(pair[1]), pairs))

    diffs = [abs(left - rhs[index]) for index, left in enumerate(lhs)]

    print("part 1:", sum(diffs))

    similarity_scores = [len(list(filter(lambda el: el == value, rhs))) for value in lhs]
    similarity_score = sum([value * similarity_scores[index] for index, value in enumerate(lhs)])

    print("part 2:", similarity_score)
