import os
from collections import deque

def get_dirs():
    return [(1, 0), (-1, 0), (0, 1), (0, -1)]

def is_region_adjacent(r1, r2):
    return (r1[1] == r2[1] and abs(r1[2] - r2[2]) == 1) or (r1[2] == r2[2] and abs(r1[1] - r2[1]) == 1)

def get_region_at(garden, starting_point):
    frontier = deque([starting_point])
    seen = set([starting_point])
    region = set()
    dirs = get_dirs()
    max_h = max(map(lambda p: p[1], garden))
    max_w = max(map(lambda p: p[2], garden))

    while frontier:
        current = frontier.popleft()

        if current[0] == starting_point[0]:
            region.add(current)

        for dir in dirs:
            next_y = current[1] + dir[0]
            next_x = current[2] + dir[1]
            in_bounds = next_y >= 0 and next_y <= max_h and next_x >= 0 and next_x <= max_w

            if in_bounds and garden_map[next_y][next_x] == current[0] and (garden_map[next_y][next_x], next_y, next_x) not in seen:
                point_at_dir = (garden_map[next_y][next_x], next_y, next_x)
                frontier.append(point_at_dir)
                seen.add(point_at_dir)

    return region

def get_garden_groups(garden):
    regions = []
    seen = set()

    for point in garden:
        if point not in seen:
            region = get_region_at(garden, point)
            regions.append(region)
            seen.update(region)

    return regions

def get_fence_cost(garden_group):
    area = len(garden_group)
    dirs = get_dirs()

    perimiter = len(list(filter(
        lambda point: point not in garden_group,
        [
            point for points in (
            list(map(lambda d: (cell[0], cell[1] + d[0], cell[2] + d[1]), dirs)) for cell in garden_group
            ) for point in points
        ]
    )))

    print("Region of {} plants with price {} * {} = {}".format(list(garden_group)[0][0], area, perimiter, area * perimiter))

    return area * perimiter

def get_fence_cost_by_number_of_sides(garden_group):
    return 0

with open(os.path.join(os.path.dirname(__file__), 'data/day12_example.txt')) as input:
    garden_map = [list(line) for line in input.read().splitlines()]
    with_coords = [(region, y, x) for y, row in enumerate(garden_map) for x, region in enumerate(row)]

    print("Part 1:", sum(map(get_fence_cost, get_garden_groups(with_coords))))
    print("Part 2:", sum(map(get_fence_cost_by_number_of_sides, get_garden_groups(with_coords))))

