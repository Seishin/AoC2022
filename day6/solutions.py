with open('input', 'r') as file:
    input = file.readline()


def get_message_start_idx(input, length):
    idx = 0
    for i in range(0, len(input) - 1):
        items = input[i:i+length]
        if len(set(items)) == len(items) == length:
            idx = i + length
            break
    return idx


def solution_1():
    return get_message_start_idx(input, 4)


def solution_2():
    return get_message_start_idx(input, 14)


def main():
    print("First part answer is: " + str(solution_1()))
    print("Second part answer is: " + str(solution_2()))


if __name__ == "__main__":
    main()
