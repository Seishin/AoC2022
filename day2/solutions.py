with open('input') as file:
    rounds = file.read().split('\n')

def solution_1():
    return sum(
        map(lambda round: {
            'A X': 4,
            'A Y': 8,
            'A Z': 3,
            'B X': 1,
            'B Y': 5,
            'B Z': 9,
            'C X': 7,
            'C Y': 2,
            'C Z': 6
        }.get(round), rounds)
    )


def solution_2():
    return sum(
        map(lambda round: {
            'A X': 3,
            'B X': 1,
            'C X': 2,
            'A Y': 4,
            'B Y': 5,
            'C Y': 6,
            'A Z': 8,
            'B Z': 9,
            'C Z': 7  
        }.get(round), rounds)
    )


def main():
    selection = int(input("Select a solution: "))
    if (selection == 1):
        print("The answer is: " + str(solution_1()))
    elif (selection == 2):
        print("The answer is: " + str(solution_2()))
    else:
        print("Select 1 or 2.")


if __name__ == "__main__":
    main()
