import os
from itertools import chain, zip_longest

def compact_filesystem(filesystem):
    indexed_filesystem = list(enumerate(filesystem))
    data_blocks = [int(block[1]) for block in indexed_filesystem if block[0] % 2 == 0]
    free_space = [int(block[1]) for block in indexed_filesystem if block[0] % 2 != 0]

    index = 0

    uncompressed_data = [data_block for data_block in enumerate(data_blocks)]
    compressed_data = []

    while len(uncompressed_data) > 0:
        compressed_data.append(uncompressed_data[0])
        del uncompressed_data[0]

        if len(uncompressed_data) > 0:
            n_from_end = int(free_space[index])

            while n_from_end > 0 and len(uncompressed_data) > 0:
                last_block = uncompressed_data[-1]

                if last_block[1] > n_from_end:
                    compressed_data.append((last_block[0], n_from_end))
                    del uncompressed_data[-1]
                    uncompressed_data.append((last_block[0], last_block[1] - n_from_end))
                    n_from_end = 0
                else:
                    compressed_data.append(last_block)
                    del uncompressed_data[-1]
                    n_from_end -= last_block[1]

        index += 1

    return compressed_data

def compact_filesystem_by_blocks(filesystem):
    indexed_filesystem = list(enumerate(filesystem))
    data_blocks = [int(block[1]) for block in indexed_filesystem if block[0] % 2 == 0]
    free_space = [int(block[1]) for block in indexed_filesystem if block[0] % 2 != 0]

    indexed_data_blocks = [data_block for data_block in enumerate(data_blocks)]
    blocks = list(chain.from_iterable(zip_longest(
        indexed_data_blocks,
        [(".", free_space_length) for free_space_length in free_space],
        fillvalue = (".", 0),
    )))

    for id_to_move in range(indexed_data_blocks[-1][0], 0, -1):
        data_block_to_move = next((b for b in enumerate(blocks) if b[1][0] == id_to_move), None)

        first_free_space_that_fits = next((
            free_space_block for free_space_block in enumerate(blocks)
            if free_space_block[1][0] == "." 
                and free_space_block[1][1] >= data_block_to_move[1][1] 
                and free_space_block[0] < data_block_to_move[0]
        ), None)

        if first_free_space_that_fits is not None:
            data_block_size = data_block_to_move[1][1]
            remaining_free_space = first_free_space_that_fits[1][1] - data_block_size
            blocks[first_free_space_that_fits[0]] = (data_block_to_move[1][0], data_block_size)
            blocks[data_block_to_move[0]] = (first_free_space_that_fits[1][0], data_block_size)

            if first_free_space_that_fits[1][1] > data_block_size:
                blocks.insert(first_free_space_that_fits[0] + 1, (".", remaining_free_space))

    return blocks

def calculate_checksum(filesystem):
    blocks = [[block[0]] * block[1] for block in filesystem]
    flat_blocks = [block for block_repeated in blocks for block in block_repeated]

    return sum([block[0] * block[1] if block[1] != "." else 0 for block in enumerate(flat_blocks)])

def debug(filesystem):
    blocks = [[block[0]] * block[1] for block in filesystem]
    flat_blocks = [str(block) for block_repeated in blocks for block in block_repeated]

    print(''.join(flat_blocks))

with open(os.path.join(os.path.dirname(__file__), "data/day9.txt")) as input:
    disk_map = input.read().rstrip("\n")

    print("Part 1:", calculate_checksum(compact_filesystem(disk_map)))
    print("Part 2:", calculate_checksum(compact_filesystem_by_blocks(disk_map)))
