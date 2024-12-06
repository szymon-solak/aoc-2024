import os

def get_starting_point(lab_map):
    for row_index, row in enumerate(lab_map):
        for column_index, column in enumerate(row):
            if column == "^":
                return (row_index, column_index)

def dir_to_vector(dir):
    match dir:
        case "^":
            return (-1, 0)
        case "v":
            return (1, 0)
        case "<":
            return (0, -1)
        case ">":
            return (0, 1)

def get_next_dir(dir):
    match dir:
        case "^":
            return ">"
        case "v":
            return "<"
        case "<":
            return "^"
        case ">":
            return "v"

def traverse_lab(lab_map, starting_point):
    steps = [starting_point]
    dir = lab_map[starting_point[0]][starting_point[1]]

    while True:
        vec = dir_to_vector(dir)
        next_step = (steps[-1][0] + vec[0], steps[-1][1] + vec[1])

        if next_step[0] >= len(lab_map) or next_step[1] >= len(lab_map[0]):
            break

        if lab_map[next_step[0]][next_step[1]] == "#":
            dir = get_next_dir(dir)
        else:
            steps.append(next_step)

    return steps

with open(os.path.join(os.path.dirname(__file__), 'data/day6.txt')) as input:
    lab_map = [list(line) for line in input.read().splitlines()]
    starting_point = get_starting_point(lab_map)
    guard_path = traverse_lab(lab_map, starting_point)

    print("Part 1:", len(set(guard_path)))

