import networkx as nx
import sys
import fileinput

from occupations import gen_moves, gen_occupations, create_edge_matrix, print_matrix
from file_handling import file_import, test_import, process_input
from graph import create_graph, bfs_shortest_path

def print_hi(name):
    print(f'Hi, {name}')

def main():
    print("Hellow there") ##test
    # file_info = file_import() ##this is where we will import the command line file

    ##where file_info is a tuple containing dimensions, node_colors, start_positions, and edges
    file_info = test_import()
    # print(file_info)

    edge_color_matrix = create_edge_matrix(file_info[0], file_info[3])
    # print_matrix(edge_color_matrix)

    occupations = gen_occupations(file_info[0])

    moves = gen_moves(occupations, edge_color_matrix, file_info[1])

    g = create_graph(moves)

    ##set finish condition
    start = str(file_info[2][0]) + " " + str(file_info[2][1])
    target_digit = 8
    shortest_path = bfs_shortest_path(g, start, target_digit)
    #print(shortest_path)






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


