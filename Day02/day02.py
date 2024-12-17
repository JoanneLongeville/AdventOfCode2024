# Part 01

def import_input(file):
    with open(file, 'r') as file:
        input = [list(map(int, line.split())) for line in file if line.strip()]
    return input


def is_valid_difference(diff):
    return diff in {-3, -2, -1, 1, 2, 3}


def safe_reports_count(input):
    safe_count = 0
    for report in input:
        differences = []
        for i in range(1, len(report)):
            diff = report[i] - report[i-1]
            differences.append(diff)
        all_positive = all(diff > 0 for diff in differences)
        all_negative = all(diff < 0 for diff in differences)
        valid_differences = all(is_valid_difference(diff) for diff in differences)
        if (all_positive or all_negative) and valid_differences:
            safe_count += 1
    return safe_count


def test_part_one():
    input = import_input('input_test.yml')
    return safe_reports_count(input)


print('test_part_one: ', test_part_one())


def part_one():
    input = import_input('input.yml')
    return safe_reports_count(input)


print('part_one: ', part_one())


# Part 02


def test_part_two():
    return


print('test_part_two: ', test_part_two())


def part_two():
    return


print('part_two: ', part_two())
