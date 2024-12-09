import os

def get_antinodes(source_antenna, antennas):
    antennas_of_same_frequency = filter(
        lambda antenna: antenna[0] == source_antenna[0] and antenna is not source_antenna,
        antennas
    )
    antinodes = map(
        lambda antenna: (
            antenna[1] + (antenna[1] - source_antenna[1]),
            antenna[2] + (antenna[2] - source_antenna[2])
        ),
        antennas_of_same_frequency
    )

    return antinodes

def is_antinode_in_bounds(antinode, antennas_map):
    return antinode[0] >= 0 and antinode[0] < len(antennas_map) and antinode[1] >= 0 and antinode[1] < len(antennas_map[0])

def get_resonant_antinodes(source_antenna, antennas, antennas_map):
    antennas_of_same_frequency = list(filter(
        lambda antenna: antenna[0] == source_antenna[0] and antenna is not source_antenna,
        antennas
    ))

    antinodes = [(antenna[1], antenna[2]) for antenna in antennas_of_same_frequency]

    for antenna in antennas_of_same_frequency:
        last_pos = (antenna[1], antenna[2])
        distance = (antenna[1] - source_antenna[1], antenna[2] - source_antenna[2])

        while True:
            next_antinode = (last_pos[0] + distance[0], last_pos[1] + distance[1])

            if not is_antinode_in_bounds(next_antinode, antennas_map):
                break

            antinodes.append(next_antinode)
            last_pos = next_antinode

    return antinodes

with open(os.path.join(os.path.dirname(__file__), 'data/day8.txt')) as input:
    antennas_map = [list(line) for line in input.read().splitlines()]
    antennas = [
        (antenna, y, x)
        for (y, antenna_row) in enumerate(antennas_map)
        for (x, antenna) in enumerate(antenna_row)
        if antenna != '.'
    ]
    antinodes = set([
        antinode 
        for antenna_antinodes in map(lambda antenna: list(get_antinodes(antenna, antennas)), antennas)
        for antinode in antenna_antinodes
    ])
    antinodes_in_bounds = filter(
        lambda antinode: is_antinode_in_bounds(antinode, antennas_map),
        antinodes,
    )

    print("Part 1:", len(list(antinodes_in_bounds)))

    resonant_antinodes = set([
        antinode 
        for antenna_antinodes in map(lambda antenna: list(get_resonant_antinodes(antenna, antennas, antennas_map)), antennas)
        for antinode in antenna_antinodes
    ])

    print("Part 2:", len(list(resonant_antinodes)))

