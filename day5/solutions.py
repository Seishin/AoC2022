import re
from copy import deepcopy

with open('input', 'r') as file:
    input = list(file.read().split('\n\n'))

def prepare(input):
    copy = deepcopy(input)

    rows = copy[0].split('\n')
    positions = rows[len(rows) - 1]
    last_position = int(positions[len(positions) - 2])

    columns = {}

    for position in range(1, last_position + 1):
        position_index = positions.index(str(position))

        columns[position] = []

        for x in range(0, len(rows) - 1):
            crate = rows[x][position_index]
            if crate != ' ': columns[position].append(crate)

        columns[position].reverse()

    steps = list(map(lambda x: re.findall(r'\d+', x), copy[1].split('\n')))

    return [columns, steps]

def pop(arr, from_pos, to_pos, n = 1):
    if n > 1:
        items = arr[from_pos][-n:]
        del arr[from_pos][len(arr[from_pos]) - n:]
        arr[to_pos].extend(items)
    else:
        item = arr[from_pos].pop()
        arr[to_pos].append(item)

def solution_1():
    columns, steps = prepare(input)

    for step in steps:
        items_to_move = int(step[0])
        from_pos = int(step[1])
        to_pos = int(step[2])

        for c in range(0, items_to_move): 
            pop(columns, from_pos, to_pos)

    return ''.join([values.pop() for keys, values in columns.items()])

def solution_2():
    columns, steps = prepare(input)

    for step in steps:
        count = int(step[0])
        from_pos = int(step[1])
        to_pos = int(step[2])
        
        pop(columns, from_pos, to_pos, count)

    return ''.join([values.pop() for keys, values in columns.items()])


def main():
    print("First part answer is: " + str(solution_1()))
    print("Second part answer is: " + str(solution_2()))


if __name__ == "__main__":
    main()
