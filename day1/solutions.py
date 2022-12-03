with open('input', 'r') as file:
    items = list(file.read().split('\n'))

grouped = [[]]
for item in items:
    grouped.append([]) if (item == "") else grouped[len(
        grouped) - 1].append(int(item))


def solution_1():
    return max([sum(x) for x in grouped])


def solution_2():
    return sum(sorted([sum(x) for x in grouped], reverse=True)[:3])


def main():
    print("First part answer is: " + str(solution_1()))
    print("Second part answer is: " + str(solution_2()))


if __name__ == "__main__":
    main()
