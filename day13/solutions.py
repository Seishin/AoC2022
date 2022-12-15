from copy import deepcopy

with open('input', 'r') as file:
    file = file.read()
    puzzle_1_input = list(map(lambda z: [eval(z[0]), eval(z[1])], map(lambda x: x.split('\n'), deepcopy(file).split("\n\n"))))
    puzzle_2_input = list(map(lambda z: eval(z), filter(lambda x: x != '', deepcopy(file).split("\n"))))

def compare(left, right):
    max_len = max(len(left), len(right))

    for i in range(max_len):
        if i >= len(left):  return 1
        if i >= len(right): return 0

        is_ordered = None

        if isinstance(left[i], int) and isinstance(right[i], int):
            if left[i] < right[i]: is_ordered = True
            if left[i] > right[i]: is_ordered = False
        elif isinstance(left[i], int) and isinstance(right[i], list):
            is_ordered = compare([left[i]], right[i])
        elif isinstance(left[i], list) and isinstance(right[i], int):
            is_ordered = compare(left[i], [right[i]])
        elif isinstance(left[i], list) and isinstance(right[i], list):
            is_ordered = compare(left[i], right[i])
        
        if is_ordered != None: return is_ordered

    return None

def solution_1():
    right_ordered_indices = []
    for pair in puzzle_1_input:
        if compare(pair[0], pair[1]):
            right_ordered_indices.append(puzzle_1_input.index(pair) + 1)
    
    return sum(right_ordered_indices)

def solution_2():
    start_index = 1
    end_index = 2

    for item in puzzle_2_input:
        if compare(item, [[2]]): start_index += 1
        if compare(item, [[6]]): end_index += 1

    return start_index * end_index

def main():
    print("First part answer is: " + str(solution_1()))
    print("Second part answer is: " + str(solution_2()))

if __name__ == "__main__":
    main()
