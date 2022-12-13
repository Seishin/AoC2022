with open('input', 'r') as file:
    input = list(map(lambda x: [c for c in x], list(file.read().split('\n'))))
    MAX_X = len(input[0])
    MAX_Y = len(input)

class Node:
    def __init__(self, x, y, elevation) -> None:
        self.x = x
        self.y = y
        self.elevation = elevation
        self.paths = []
    
    def generate_paths(self, graph):
        paths = [
            (self.x, self.y + 1),
            (self.x, self.y - 1),
            (self.x - 1, self.y),
            (self.x + 1, self.y)
        ]


        for path in paths:
            if path in graph and graph[path].elevation <= self.elevation + 1:
                self.paths.append(path)
    
    def __repr__(self) -> str:
        return "({:1},{:1})-{:1}-{:1}".format(str(self.x), str(self.y), str(self.elevation), chr(self.elevation))

def bfs(graph, start_position, end_position):
    queue = [start_position]
    visited_paths = {}
    visited_paths[start_position] = None

    while queue:
        current_position = queue.pop(0)
        if current_position == end_position: 
            break

        for next_position in graph[current_position].paths:
            if next_position not in visited_paths:
                queue.append(next_position)
                visited_paths[next_position] = current_position

    current_position = end_position
    path = []

    while current_position != start_position:
        path.append(current_position)
        
        try:
            current_position = visited_paths[current_position]
        except KeyError:
            return [False, visited_paths]
    
    return [True, len(path)]

def prepare_graph():
    graph = {}
    start_position = None
    end_position = None

    for y in range(MAX_Y):
        for x in range(MAX_X):
            value = input[y][x]
            elevation = 0

            if value == "S":
                start_position = (x, y)
                elevation = ord("a")
            elif value == "E":
                end_position = (x, y)
                elevation = ord("z")
            else:
                elevation = ord(value)

            graph[(x, y)] = Node(x, y, elevation)

    for node in graph: 
        graph[node].generate_paths(graph)
    
    return [graph, start_position, end_position]


def solution_1():
    graph, start_position, end_position = prepare_graph()

    return bfs(graph, start_position, end_position)[1]

def solution_2():
    graph, _, end_position = prepare_graph()
    paths = []

    outer_edges = []
    outer_edges.extend((i, 0) for i in range(MAX_X - 1))
    outer_edges.extend((i, MAX_Y - 1) for i in range(MAX_X - 1))
    outer_edges.extend((0, i) for i in range(MAX_Y - 1))
    outer_edges.extend((MAX_X - 1, i) for i in range(MAX_Y - 1))
    outer_edges = list(filter(lambda x: graph[x].elevation == ord('a'), graph))
    
    for position in outer_edges:
        result = bfs(graph, position, end_position)
        if result[0]:
            paths.append(result[1])
    
    return min(paths)

def main():
    print("First part answer is: " + str(solution_1()))
    print("Second part answer is: " + str(solution_2()))


if __name__ == "__main__":
    main()
