from math import ceil

with open('input', 'r') as file:
    input = file.read().split('\n')

    instructions = []
    cycle = 1
    for line in input:
        parts = line.split(' ')
        instructions.append((cycle, 0))

        if len(parts) == 2:
            cycle += 1
            instructions.append((cycle, int(parts[1])))

        cycle += 1


def solution_1():
    X_value = 1
    signal_strength = 0

    for instruction in instructions:
        cycle = instruction[0]
        signal_strength += X_value * cycle if cycle % 40 == 20 else 0
        X_value += instruction[1]

    return signal_strength


def render_screen(screen, width, height):
    screen = ''.join(screen)

    s = ''
    for i in range(height):
        s += screen[i * width: i * width + width] + "\n"

    return s[:-1]


def sprite_at(position):
    return (position - 1, position, position + 1)


def solution_2():
    WIDTH = 40
    HEIGHT = 6

    screen = ['.'] * WIDTH * HEIGHT
    X_value = 1
    sprite = sprite_at(1)

    for instruction in instructions:
        cycle, value = instruction

        if (cycle - 1) % WIDTH in sprite:
            screen[cycle - 1] = '#'

        X_value += value
        sprite = sprite_at(X_value)

    return render_screen(screen, WIDTH, HEIGHT)


def main():
    print("First part answer is: " + str(solution_1()))
    print("Second part answer is: \n" + solution_2())


if __name__ == "__main__":
    main()
