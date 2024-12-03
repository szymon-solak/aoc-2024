import os
import re
from pprint import pprint

def mul(mul_string):
    (lhs, rhs) = re.findall(r"\d+", mul_string)
    return int(lhs) * int(rhs)

with open(os.path.join(os.path.dirname(__file__), 'data/day3.txt')) as input:
    memory = input.read()
    
    muls = re.findall(r"mul\(\d+,\d+\)", memory)
    print("Part 1:", sum(map(mul, muls)))

    only_do_blocks = filter(lambda block: not block.startswith("don't()"), re.findall(r".+?(?=do\(\)|don't\(\))", ''.join(memory.splitlines())))
    only_do_muls = re.findall(r"mul\(\d+,\d+\)", ' '.join(only_do_blocks))
    print("Part 2:", sum(map(mul, only_do_muls)))
