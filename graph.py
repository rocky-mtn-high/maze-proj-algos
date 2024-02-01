import networkx as nx
from networkx import all_shortest_paths

def create_graph(moves):
    G = nx.DiGraph()
    concat_moves = []
    for move in moves:
        # if move == [[7, 7], [7,5]]:
        #     print("It exists here")
        concat_moves.append([str(move[0][0]) + " " + str(move[0][1]), str(move[1][0]) + " " + str(move[1][1]) ])

    G.add_edges_from(concat_moves)
    # print(G)
    return G

def bfs_shortest_path(graph, start, target):
    paths = []
    for node in graph.nodes():
        if str(target) in node:
            try:
                p = all_shortest_paths(graph, start, node)
                paths_list = list(p)
                # print(paths_list)
                for path in paths_list:
                    paths.append(path)
            except nx.NetworkXNoPath:
                x = 0
                # print(f"No path from {start} to {node}")


    return paths



#this proves that the path is valid and exists in valid paths. therefore there is something wrong with my BFS algorithm.
# def find_all_paths(graph, start, target):
#     all_paths = list(nx.all_simple_paths(graph, source=start, target=target))
#     return all_paths
#
# def bfs_shortest_path(graph, start, target):
#     paths = []
#     for node in graph.nodes():
#         if str(target) in node:
#             p = find_all_paths(graph, start, node)
#             paths.append(p)
#     # print(paths)
#     return(paths)



#not here
def convert_to_moves(path):
    moves = ""
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
    shortest_length = min(len(path) for path in paths)
    shortest_paths = [path for path in paths if len(path) == shortest_length]
    shortest_moves = [convert_to_moves(path) for path in shortest_paths]
    # print(shortest_moves)
    ##choose first alphabetically for shortest_move
    # return(shortest_moves)
    sorted_codes = sorted(shortest_moves, key=custom_sort)
    return sorted_codes[0]
    # return 0