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
    moves = []
    for i in range(len(path) - 1):
        current_point = path[i].split()
        next_point = path[i + 1].split()
        if current_point[0] == next_point[0] or current_point[0] == next_point[1]:
            moves.append(str(next_point[1]) + "L")
        elif current_point[1] == next_point[1] or current_point[1] == next_point[0] :
            moves.append(str(next_point[0]) + "R")

    last_move = path[-1].split()
    moves.append(last_move)

    return moves


def path_process(paths):
    shortest_length = min(len(path) for path in paths)
    shortest_paths = [path for path in paths if len(path) == shortest_length]
    shortest_moves = [convert_to_moves(path) for path in shortest_paths]


    return shortest_moves