from functools import reduce

with open('input') as file:
    contents = file.read().split('\n')


def get_priority(item):
    return ord(item) - 96 if item.islower() else ord(item) - 38


def get_common_items(first, second):
    return ''.join(set(first).intersection(second))


def map_content(content):
    first_part = content[:len(content) // 2]
    second_part = content[len(content) // 2:]

    return get_priority(get_common_items(first_part, second_part))


def solution_1():
    return sum(map(map_content, contents))


def solution_2():
    groups_of_three = [contents[i:i + 3] for i in range(0, len(contents), 3)]

    return sum(map(get_priority, [reduce(get_common_items, group) for group in groups_of_three]))


def main():
    print("First part answer is: " + str(solution_1()))
    print("Second part answer is: " + str(solution_2()))


if __name__ == "__main__":
    main()
