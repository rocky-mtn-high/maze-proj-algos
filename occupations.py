import time
import itertools


def gen_occupations(dimensions):
    node_num = int(dimensions[0])
    occupations = []

    for i in range(1, node_num + 1):
        for j in range(1, node_num + 1): ##change back to i+1
            occupations.append([i, j])
    # print(occupations)
    return occupations

def gen_moves(occup, edge_mapping, node_colors):
    start_time = time.time()

    move_count = 0
    move_list = []

    num_nodes = len(node_colors) + 1
    node_colors_set = set(node_colors)
    occup_set = {(item[0], item[1]) for item in occup}


    last = 0

    for occup_i in occup_set:
        # cp = time.time() - start_time - last
        # print("One big loop: ", cp)

        last = time.time() - start_time
        if num_nodes in occup_i:
            continue

        for occup_j in occup_set - {occup_i}:
            if occup_i[0] == occup_j[0]:
                shared, fr, to = occup_i[0], occup_i[1], occup_j[1]
            elif occup_i[1] == occup_j[1]:
                shared, fr, to = occup_i[1], occup_i[0], occup_j[0]
            else:
                continue

            if fr == num_nodes or shared == num_nodes:
                continue

            if (str(fr), str(to)) not in edge_mapping:
                continue

            move_color = edge_mapping.get((str(fr), str(to)))

            if move_color is None:
                continue

            node_color = node_colors[shared - 1]

            if move_color != node_color:
                continue

            move_count += 1
            move_list.append([occup_i, occup_j])

    print("Total loop time:", time.time() - start_time )
    return move_list



# def gen_moves(occup, edge_mapping, node_colors):
#     move_count = 0
#     move_list = []
#     node_colors_len = len(node_colors)
#     occup_len = len(occup)
#     # print(node_colors)
#     # print_matrix(edge_matrix)
#     for i in range(occup_len):
#         for j in range(occup_len):
#             occup_i, occup_j = occup[i], occup[j]
#             if occup_i[0] == occup_j[0]:
#                 shared, fr, to = occup_i[0], occup_i[1], occup_j[1]
#             elif occup_i[1] == occup_j[1]:
#                 shared, fr, to = occup_i[1], occup_i[0], occup_j[0]
#             else:
#                 continue
#             if fr == node_colors_len + 1:
#                 continue
#             move_color = edge_mapping.get((str(fr), str(to)))
#
#             if move_color is None or shared == node_colors_len + 1:
#                 continue
#             node_color = node_colors[shared - 1]
#             # print("Node " + str(shared) + ": " + node_color)
#
#             if move_color != node_color:
#                 # print(shared)
#                 # print("The edge from " + str(fr) + " to " + str(to) + " is color " + move_color + " when it should be " + node_color)
#                 continue
#
#             move_count += 1
#             move_list.append([occup_i, occup_j])
#     # print("total valid moves = " + str(move_count))
#     # print(move_list)
#     return move_list

def create_edge_mapping(edge_list):
    mapping = {}
    for edge in edge_list:
        pair = (edge[0], edge[1])
        letter = edge[2]
        mapping[pair] = letter
    return mapping



def print_matrix(matrix):
    for row in matrix:
        r = ""
        for elm in row:
            r = r + str(elm)
        print(r)
    return 0