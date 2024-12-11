# Part 01

def import_input(file):
    with open(file, 'r') as file:
        input = [list(map(int, line.split())) for line in file if line.strip()]
    return input


def pair_up(data):
    left = sorted([row[0] for row in data])
    rght = sorted([row[1] for row in data])
    paired = list(zip(left, rght))
    return paired


def pair_differences(pairs):
    differences = [abs(pair[0] - pair[1]) for pair in pairs]
    return differences


def sum_differences(differences):
    return sum(differences)


def test_part_one():
    locations = import_input('input_test.yml')
    locations = pair_up(locations)
    locations = pair_differences(locations)
    locations = sum_differences(locations)
    return locations


print('test_part_one: ', test_part_one())


def part_one():
    locations = import_input('input.yml')
    locations = pair_up(locations)
    locations = pair_differences(locations)
    locations = sum_differences(locations)
    return locations


print('part_one: ', part_one())


# Part 02


def test_part_two():
    locations = import_input('input_test.yml')
    left = [row[0] for row in locations]
    rght = [row[1] for row in locations]
    score = 0
    for num in left:
        score += num * rght.count(num)
    return score


print('test_part_two: ', test_part_two())


def part_two():
    locations = import_input('input.yml')
    left = [row[0] for row in locations]
    rght = [row[1] for row in locations]
    score = 0
    for num in left:
        score += num * rght.count(num)
    return score


print('part_two: ', part_two())
