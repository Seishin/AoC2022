with open('input', 'r') as file:
    items = list(file.read().split('\n'))

grouped = [[]]
for item in items: grouped.append([]) if (item == "") else grouped[len(grouped) - 1].append(int(item))

def solution1():
    return max([sum(x) for x in grouped])

def solution2():
    return sum(sorted([sum(x) for x in grouped], reverse=True)[:3])

def main():
    selection = int(input("Select a solution: "))
    if (selection == 1):
        print("The answer is: " + str(solution1()))
    elif (selection == 2):
        print("The answer is: " + str(solution2()))
    else:
        print("Select 1 or 2.")

if __name__ == "__main__":
    main()