with open('input', 'r') as file:
    assignments = list(file.read().split('\n'))


def solution_1():
    overlaps = 0

    for assignment in assignments:
        first, second = assignment.split(',')

        first_start, first_end = map(lambda x: int(x), first.split('-'))
        second_start, second_end = map(lambda x: int(x), second.split('-'))

        overlaps += 1 if (first_start >= second_start and first_end <= second_end) or (
            second_start >= first_start and second_end <= first_end) else 0

    return overlaps


def solution_2():
    overlaps = 0

    for assignment in assignments:
        first, second = assignment.split(',')

        first_start, first_end = map(lambda x: int(x), first.split('-'))
        second_start, second_end = map(lambda x: int(x), second.split('-'))

        first = [x for x in range(first_start, first_end + 1)]
        second = [x for x in range(second_start, second_end + 1)]

        overlaps += 1 if len(list(set(first).intersection(second))) > 0 else 0

    return overlaps


def main():
    print("First part answer is: " + str(solution_1()))
    print("Second part answer is: " + str(solution_2()))


if __name__ == "__main__":
    main()
