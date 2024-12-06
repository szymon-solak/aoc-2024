import os
from functools import cmp_to_key

def is_update_ordered(update, rules):
    rules_for_pages = [rule for rule in rules if rule[0] in update]

    for rule in rules_for_pages:
        try:
            if update.index(rule[1]) < update.index(rule[0]):
                return False
        except ValueError:
            continue

    return True

def sort_update(update, rules):
    rules_for_pages = [rule for rule in rules if rule[0] in update]

    def compare(lhs, rhs):
        rule = next((r for r in rules_for_pages if lhs in r and rhs in r), None)
        
        if rule is None: return 0
        if rule[0] == lhs: return -1
        return 1

    return sorted(update, key = cmp_to_key(compare))

with open(os.path.join(os.path.dirname(__file__), 'data/day5.txt')) as input:
    (rules_input, updates_input) = input.read().split("\n\n")
    rules = [list(map(int, rule.split("|"))) for rule in rules_input.splitlines()]
    updates = [list(map(int, update.split(","))) for update in updates_input.splitlines()]
    
    ordered_updates = filter(lambda update: is_update_ordered(update, rules), updates)
    middle_items = map(lambda update: update[len(update) // 2], ordered_updates)

    print("Part 1:", sum(middle_items))

    incorrectly_ordered_updates = filter(lambda update: not is_update_ordered(update, rules), updates)
    middle_items_from_incorrect = map(lambda update: sort_update(update, rules)[len(update) // 2], incorrectly_ordered_updates)

    print("Part 2:", sum(middle_items_from_incorrect))

