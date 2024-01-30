import networkx as nx
import sys
import fileinput

from occupations import gen_moves, gen_occupations,print_matrix, create_edge_mapping
from file_handling import file_import, test_import, process_input
from graph import create_graph, bfs_shortest_path, path_process

def print_hi(name):
    print(f'Hi, {name}')

def main():
    # file_info = file_import() ##this is where we will import the command line file

    ##where file_info is a tuple containing dimensions, node_colors, start_positions, and edges
    file_info = test_import()
    # print(file_info)

    # edge_color_matrix = create_edge_matrix(file_info[0], file_info[3])
    # print_matrix(edge_color_matrix)

    occupations = gen_occupations(file_info[0])

    edge_color_list = file_info[3]
    mapping = create_edge_mapping(edge_color_list)
    # print(mapping)
    moves = gen_moves(occupations, mapping, file_info[1])

    g = create_graph(moves)


    # set finish condition
    start = str(file_info[2][0]) + " " + str(file_info[2][1])
    target_digit = file_info[0][0]
    # print(target_digit)
    paths = bfs_shortest_path(g, start, target_digit)
    # print(paths)
    if paths == []:
        print("NO PATH")
    else:
        best = path_process(paths, start)
        print(best)







# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


