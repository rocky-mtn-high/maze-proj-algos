import networkx as nx
import sys
import fileinput
import time
import cProfile

from occupations import gen_moves, gen_occupations,print_matrix, create_edge_mapping
from file_handling import file_import, test_import, process_input
from graph import create_graph, bfs_shortest_path, path_process
from moves import create_node_dictionary, create_moves
def print_hi(name):
    print(f'Hi, {name}')


def convert_to_moves(path):
    moves = ""
    for i in range(len(path) - 1):
        if i == 0:
            next = path[0]
        curr = next
        next = path[i+1]

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

def main():
    profiler = cProfile.Profile()
    profiler.enable()

    file_info = test_import()
    # file_info = file_import()

    nodes = file_info[1]
    edges = file_info[3]
    mapping = {}
    node_num = len(nodes)
    for edge in edges:
        fr = edge[0]
        to = edge[1]
        e_color = edge[2]

        if (fr, to) not in mapping:
            mapping[(fr, to)] = []

        for i in range(node_num):
            node_color = nodes[i]
            if node_color == e_color:
                mapping[(fr, to)].append(i + 1)


    #create graph as we discover edges

    G = nx.DiGraph()

    start = file_info[2]
    finish = file_info[0][0]
    move_ct = 0
    moves = []
    for key in mapping:
        valid_from = mapping[key]
        for fr in valid_from:
            G.add_edge((int(key[0]), fr), (int(key[1]), fr))
            G.add_edge((fr, int(key[0])), (fr, int(key[1])))
    # print(G.edges())

    #now we search
    target_digit = int(file_info[0][0])
    start = (int(file_info[2][0]),  int(file_info[2][1]))
    new_paths = bfs_shortest_path(G, start, target_digit)
    if new_paths == []:
        print("NO PATH")
    else:
        best = path_process(new_paths, start)
        print(best)

    profiler.disable()
    profiler.print_stats(sort='cumulative')


# def main():
#     # profiler = cProfile.Profile()
#     # profiler.enable()
#
#
#     # start_time = time.time()
#     # file_info = file_import() ##this is where we will import the command line file
#
#     ##where file_info is a tuple containing dimensions, node_colors, start_positions, and edges
#     # file_info = test_import()
#
#     # cp1 = time.time() - start_time
#     # print("Importing and processing file: ", cp1 )
#     # print(file_info)
#
#     # dict = create_node_dictionary(file_info[1], file_info[3] )
#
#     # start = file_info[2]
#     # finish = file_info[0][0]
#
#     # new_moves = create_moves(start, finish, dict)
#
#
#
#     # occupations = gen_occupations(file_info[0])
#     # # cp2 = time.time() - start_time - cp1
#     #
#     # # print("Generating occupations: ", cp2)
#     # edge_color_list = file_info[3]
#     #
#     #
#     # mapping = create_edge_mapping(edge_color_list)
#     #
#     # # cp3 = time.time() - start_time - cp1 -cp2
#     # # print("Creating mapping: ", cp3)
#     #
#     #
#     # # print(mapping)
#     # moves = gen_moves(occupations, mapping, file_info[1])
#     # # cp4 = time.time() - start_time - cp1 -cp2 - cp3
#     # # print("Generating moves: ", cp4)
#     #
#     #
#     # g = create_graph(moves)
#     # new_g = create_graph(new_moves)
#
#     # print("g: ", g)
#     # print("new: ", new_g)
#     # print(nx.is_isomorphic(g, new_g)) ####FUCK YES
#
#     # # cp5 = time.time() - start_time - cp1 -cp2 - cp3 - cp4
#     # # print("Creating graph: ", cp5)
#     # # set finish condition
#     # start = str(file_info[2][0]) + " " + str(file_info[2][1])
#     target_digit = file_info[0][0]
#     # # print(target_digit)
#     # paths = bfs_shortest_path(g, start, target_digit)
#     new_paths = bfs_shortest_path(new_g, start, target_digit)
#     # # print(paths)
#     if new_paths == []:
#         print("NO PATH")
#     else:
#         best = path_process(new_paths, start)
#         print(best)
#
#     profiler.disable()
#
#     # Print the profiling results
#     profiler.print_stats(sort='cumulative')








# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


