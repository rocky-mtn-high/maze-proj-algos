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

def convert_to_moves(path, start):
    r = start.split()[0]
    l = start.split()[1]
    moves = []
    # print(path)
    for i in range(len(path) - 1):
        current = path[i].split()
        next = path[i + 1].split()
        ##align them
        if next[0] != current[0] and next[0] != next[1]:
            next.reverse()
        if current[0] == next[0]:
            moves.append( "L" + str(next[1]))
        elif current[1] == next[1]:
            moves.append("R" + str(next[0]))

    # last_move = path[-1].split()
    # moves.append(last_move)

    move_string = ""
    for move in moves:
        move_string = move_string + move
    return move_string


def path_process(paths, start):
    shortest_length = min(len(path) for path in paths)
    shortest_paths = [path for path in paths if len(path) == shortest_length]
    shortest_moves = [convert_to_moves(path, start) for path in shortest_paths]
    ##choose first alphabeticaly for shortest_move
    return min(shortest_moves)