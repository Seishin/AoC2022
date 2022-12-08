from functools import reduce

with open('input', 'r') as file:
    input = list(map(lambda x: list(map(lambda y: int(y), list(x))), file.read().split('\n')))

MAX_X = len(input[0]) - 1
MAX_Y = len(input) - 1

def get_adjacent_trees(arr, x, y):
    return {
        'left': [arr[y][i] for i in range(0, x)],
        'right': [arr[y][i] for i in range(x + 1, MAX_X + 1)],
        'top': [arr[i][x] for i in range(0, y)],
        'bottom': [arr[i][x] for i in range(y + 1, MAX_Y + 1)]
    }

def solution_1():
    visible_edges = (MAX_X * 2) + (MAX_Y * 2)
    
    for y in range(1, MAX_Y):
        for x in range(1, MAX_X):
            current = input[y][x]
            adjacent_trees = get_adjacent_trees(input, x, y)

            if max(adjacent_trees['left']) < current:
                visible_edges += 1
            elif max(adjacent_trees['right']) < current:
                visible_edges += 1
            elif max(adjacent_trees['top']) < current:
                visible_edges += 1
            elif max(adjacent_trees['bottom']) < current:
                visible_edges += 1

    return visible_edges
    
def solution_2():
    scenic_scores = []

    def get_blocked_at(current, trees):
        count = 0
        for tree in trees:
            if tree < current: count += 1
            else: count += 1; break
        
        return count
    
    for y in range(1, MAX_Y):
        for x in range(1, MAX_X):
            current = input[y][x]
            adjacent_trees = get_adjacent_trees(input, x, y)

            scores = list(filter(lambda x: x > 0, [
                get_blocked_at(current, reversed(adjacent_trees['left'])),
                get_blocked_at(current, adjacent_trees['right']),
                get_blocked_at(current, reversed(adjacent_trees['top'])),
                get_blocked_at(current, adjacent_trees['bottom'])
            ]))

            scenic_scores.append(reduce(lambda a, b: a * b, scores))

    return max(scenic_scores)

def main():
    print("First part answer is: " + str(solution_1()))
    print("Second part answer is: " + str(solution_2()))


if __name__ == "__main__":
    main()