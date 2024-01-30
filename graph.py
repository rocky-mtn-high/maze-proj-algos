import networkx as nx

def create_graph(moves):
    G = nx.DiGraph()
    concat_moves = []
    for move in moves:
        concat_moves.append([str(move[0][0]) + " " + str(move[0][1]), str(move[1][0]) + " " + str(move[1][1]) ])

    G.add_edges_from(concat_moves)

    # print(G)
    return G


def bfs_shortest_path(graph, start, target_digit):
    paths = []
    visited = set()
    queue = [(start, [start])] # Queue now stores both node and its path
    visited.add(start)

    while queue:
        current_node, path = queue.pop(0)

        if str(target_digit) in current_node:
            # return path  # Found the shortest path
            paths.append(path)

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
                visited.add(neighbor)

    return paths

def convert_to_moves(path):
    moves = ""
    # print(path)
    for i in range(len(path) - 1):
        if i == 0:
            next = path[0].split()
        curr = next
        next = path[i+1].split()

        if curr[0] == next[0]:
            moves = moves + "L" + str(next[1])
        elif curr[1] == next[1]:
            moves = moves + "R" + str(next[0])
        else:
            print("This should never happen.")
            return 0
    # print(moves)
    return moves



def extract_letters(code):
    return ''.join(filter(str.isalpha, code))

def custom_sort(code):
    return extract_letters(code)


def path_process(paths, start):
    shortest_moves = 0
    shortest_length = min(len(path) for path in paths)
    shortest_paths = [path for path in paths if len(path) == shortest_length]
    shortest_moves = [convert_to_moves(path) for path in shortest_paths]
    ##choose first alphabeticaly for shortest_move
    # return(shortest_moves)
    sorted_codes = sorted(shortest_moves, key=custom_sort)
    return sorted_codes[0]