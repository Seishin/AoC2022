from math import floor, lcm
from copy import deepcopy
from input import input

def inspect(item, divisor, operation):
    operation, value = operation
    value = int(value) if value != "old" else item
    inspected_item = 0

    if operation == "+":
        inspected_item = int(floor((item + value)))
    elif operation == "-":
        inspected_item = int(floor((item - value)))
    elif operation == "*":
        inspected_item = int(floor((item * value)))
    elif operation == "/":
        inspected_item = int(floor((item / value)))
    
    if divisor != None:
        inspected_item %= divisor
    else:
        inspected_item /= 3
    
    return inspected_item

def play(monkeys, rounds, divisor):
    for i in range(0, rounds):
        for monkey in monkeys:
            for item in monkey['items']:
                item = inspect(item, divisor, monkey['operation'])
                if item % monkey['divisor'] == 0:
                    monkeys[monkey['throw_to'][0]]['items'].append(item)
                else:
                    monkeys[monkey['throw_to'][1]]['items'].append(item)
                monkey['count'] += 1
            monkey['items'] = []

    counts = list(sorted(map(lambda x: x['count'], monkeys), reverse=True))
    return counts[0] * counts[1]

def solution_1():
    monkeys = deepcopy(input)
    return play(monkeys, 20, None)

def solution_2():
    monkeys = deepcopy(input)
    least_common_multiple = lcm(*[monkey['divisor'] for monkey in monkeys])
    return play(monkeys, 10_000, least_common_multiple)

def main():
    print("First part answer is: " + str(solution_1()))
    print("Second part answer is: " + str(solution_2()))


if __name__ == "__main__":
    main()
