import os

def compact_filesystem(filesystem):
    indexed_filesystem = list(enumerate(filesystem))
    data_blocks = [int(block[1]) for block in indexed_filesystem if block[0] % 2 == 0]
    free_space = [int(block[1]) for block in indexed_filesystem if block[0] % 2 != 0]

    print(sum(data_blocks) + sum(free_space))

    return filesystem

def calculate_checksum(filesystem):
    return 0

with open(os.path.join(os.path.dirname(__file__), 'data/day9.txt')) as input:
    disk_map = input.read().rstrip("\n")

    print("Part 1:", calculate_checksum(compact_filesystem(disk_map)))

