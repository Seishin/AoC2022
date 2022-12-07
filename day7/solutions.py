with open('input', 'r') as file:
    input = list(file.read().split('\n'))
class Directory:
    def __init__(self, name, parent=None) -> None:
        self.name = name
        self.parent = parent
        self.files = []
        self.sub_dirs = []

    def size(self):
        files_size = sum(self.files)
        dirs_size = sum(map(lambda x: x.size(), self.sub_dirs))

        return files_size + dirs_size
    
    def find_dir(self, name):
        dirs = list(filter(lambda x: x.name == name, self.sub_dirs))
        if len(dirs) > 0:
            return dirs[0]
        else:
            return None

directories = []

def solution_1():
    current_dir = None

    for cmd in input:
        if cmd.startswith("dir") or cmd.startswith("$ ls"):
            continue
        elif cmd.startswith("$ cd"):
            parts = cmd.split(' ')

            if current_dir == None:
                current_dir = Directory('/')
                directories.append(current_dir)

            if parts[2] == "..":
                current_dir = current_dir.parent
            else:
                looked_dir = current_dir.find_dir(parts[2])

                if looked_dir == None:
                    new_dir = Directory(parts[2], current_dir)
                    current_dir.sub_dirs.append(new_dir)
                    directories.append(new_dir)

                    current_dir = new_dir
                else:
                    current_dir = looked_dir
        else:
            current_dir.files.append(int(cmd.split(' ')[0]))

    del directories[0]

    return sum(filter(lambda y: y < 100000, map(lambda x: x.size(), directories)))

def solution_2():
    MAX_SPACE = 70_000_000
    NEEDED_SPACE = 30_000_000

    root_space = directories[0].size()
    free_space = MAX_SPACE - root_space
    required_space = NEEDED_SPACE - free_space

    dirs_sorted = list(sorted(map(lambda x: x.size(), directories)))

    return list(filter(lambda x: x >= required_space, dirs_sorted))[0]


def main():
    print("First part answer is: " + str(solution_1()))
    print("Second part answer is: " + str(solution_2()))


if __name__ == "__main__":
    main()