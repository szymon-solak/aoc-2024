import os
import re
from itertools import pairwise

def is_report_safe(report):
    is_asc = all(x <= y for x, y in pairwise(report))
    is_desc = all(x >= y for x, y in pairwise(report))

    if not is_asc and not is_desc:
        return False

    return all(abs(x - y) >= 1 and abs(x - y) <= 3 for x, y in pairwise(report))

def is_report_safe_with_problem_dampener(report):
    for index in range(0, len(report)):
        report_without_value = list(report)
        del report_without_value[index]
        if is_report_safe(report_without_value):
            return True

    return False

with open(os.path.join(os.path.dirname(__file__), 'data/day2.txt')) as input:
    reports = [re.split(r"\s+", line) for line in input.read().splitlines()]
    unsafe_reports = [report for report in reports if not is_report_safe(list(map(int, report)))]

    print("Part 1:", len(reports) - len(unsafe_reports))

    safe_with_problem_dampener = [report for report in unsafe_reports if is_report_safe_with_problem_dampener(list(map(int, report)))]

    print("Part 2:", len(reports) - len(unsafe_reports) + len(safe_with_problem_dampener))

