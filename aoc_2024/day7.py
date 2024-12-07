import os
from itertools import combinations_with_replacement, permutations, chain, product
from functools import reduce

def calculate(numbers, operators):
    result = numbers[0]

    for op_index, op in enumerate(operators):
        match op:
            case "+":
                result = result + numbers[op_index + 1]
            case "*":
                result = result * numbers[op_index + 1]
            case "|":
                result = int("{}{}".format(result, numbers[op_index + 1]))

    return result

def is_possible(result, numbers, ops_string):
    operators = product(ops_string, repeat=len(numbers) - 1)
    any_option_resolves = next((op for op in operators if calculate(numbers, op) == result), None)

    return any_option_resolves != None

with open(os.path.join(os.path.dirname(__file__), 'data/day7.txt')) as input:
    equations_input = [line.split(": ") for line in input.read().splitlines()]
    equations = [(int(input[0]), list(map(int, input[1].split()))) for input in equations_input]

    possible_equations = filter(lambda input: is_possible(input[0], input[1], "+*"), equations)
    print("Part 1:", sum(map(lambda l: l[0], possible_equations)))

    possible_equations_with_concat = filter(lambda input: is_possible(input[0], input[1], "+*|"), equations)
    print("Part 2:", sum(map(lambda l: l[0], possible_equations_with_concat)))

