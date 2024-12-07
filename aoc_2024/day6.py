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

def traverse_lab(lab_map, starting_point, additional_blockade=(-1, -1)):
    steps = [starting_point]
    dir = lab_map[starting_point[0]][starting_point[1]]
    visited_in_dir = {}

    while True:
        vec = dir_to_vector(dir)
        next_step = (steps[-1][0] + vec[0], steps[-1][1] + vec[1])

        visited_previosly = "{}-{}-{}".format(steps[-1][0], steps[-1][1], dir) in visited_in_dir

        if visited_previosly:
            raise Exception("Infinite loop")

        visited_in_dir["{}-{}-{}".format(steps[-1][0], steps[-1][1], dir)] = True

        if next_step[0] >= len(lab_map) or next_step[1] >= len(lab_map[0]) or next_step[0] < 0 or next_step[1] < 0:
            break

        if lab_map[next_step[0]][next_step[1]] == "#" or next_step == additional_blockade:
            dir = get_next_dir(dir)
        else:
            steps.append(next_step)

    return steps

def count_loops(lab_map, starting_point, steps):
    loops = 0

    for step in list(set(steps))[1:]:
        try:
            traverse_lab(lab_map, starting_point, step)
        except Exception as ex:
            loops = loops + 1

    return loops

with open(os.path.join(os.path.dirname(__file__), 'data/day6.txt')) as input:
    lab_map = [list(line) for line in input.read().splitlines()]
    starting_point = get_starting_point(lab_map)
    guard_path = traverse_lab(lab_map, starting_point)

    print("Part 1:", len(set(guard_path)))
    print("Part 2:", count_loops(lab_map, starting_point, guard_path))

