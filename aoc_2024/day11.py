import os
from functools import lru_cache

def blink(stone):
    if stone == 0:
        return (1,)

    stone_string = str(stone)

    if len(stone_string) % 2 == 0:
        return (
            int(stone_string[: len(stone_string) // 2]),
            int(stone_string[len(stone_string) // 2 :])
        )

    return (stone * 2024,)

@lru_cache(maxsize=None)
def stone_after_blinking_n_times(stone, blinks):
    after_blinking = blink(stone)

    if blinks == 0:
        return len(after_blinking)

    return sum(
        stone_after_blinking_n_times(new_stone, blinks - 1) for new_stone in after_blinking
    )

def stones_after_blinking_n_times(stones, blinks):
    return sum(
        stone_after_blinking_n_times(stone, blinks - 1) for stone in stones
    )

with open(os.path.join(os.path.dirname(__file__), 'data/day11.txt')) as input:
    stones = list(map(int, input.read().split()))

    print("Part 1:", stones_after_blinking_n_times(stones, 25))
    print("Part 2:", stones_after_blinking_n_times(stones, 75))
