import os
from itertools import chain

def get_trailhead_paths(hiking_map, trailhead):
    val_at_trailhead = hiking_map[trailhead[0]][trailhead[1]] 

    if val_at_trailhead == 9:
        return [trailhead]

    possible_ways_to_go = map(
        lambda dir: (trailhead[0] + dir[0], trailhead[1] + dir[1]),
        [(1, 0), (-1, 0), (0, -1), (0, 1)]
    )
    possible_ways_to_go_in_bounds = filter(
        lambda point:
            point[0] >= 0 and point[0] < len(hiking_map)
            and point[1] >= 0 and point[1] < len(hiking_map[0]),
        possible_ways_to_go
    )
    possible_ways_to_go_higher = list(filter(
        lambda point: hiking_map[point[0]][point[1]] == val_at_trailhead + 1,
        possible_ways_to_go_in_bounds
    ))

    if len(possible_ways_to_go_higher) == 0:
        return []

    return list(chain.from_iterable(map(
        lambda point: get_trailhead_paths(hiking_map, point),
        possible_ways_to_go_higher
    )))

def get_trailhead_score(hiking_map, trailhead):
    return len(set(get_trailhead_paths(hiking_map, trailhead)))

def get_trailhead_rating(hiking_map, trailhead):
    return len(get_trailhead_paths(hiking_map, trailhead))

with open(os.path.join(os.path.dirname(__file__), 'data/day10.txt')) as input:
    hiking_map = [list(map(int, list(line))) for line in input.read().splitlines()]
    trailheads = [
        (y, x)
        for y, row in enumerate(hiking_map)
        for x, col in enumerate(row)
        if col == 0
    ]

    trailhead_scores = map(lambda trailhead: get_trailhead_score(hiking_map, trailhead), trailheads)
    print("Part 1:", sum(trailhead_scores))

    trailhead_ratings = map(lambda trailhead: get_trailhead_rating(hiking_map, trailhead), trailheads)
    print("Part 2:", sum(trailhead_ratings))
