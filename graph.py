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
    # Handle the case