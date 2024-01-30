def gen_occupations(dimensions):
    node_num = int(dimensions[0])
    occupations = []

    for i in range(1, node_num + 1):
        for j in range(i, node_num + 1): ##change back to i+1
            occupations.append([i, j])
    # print(occupations)
    return occupations

def gen_moves(occup, edge_mapping, node_colors):
    move_count = 0
    move_list = []
    node_colors.append('finish')
    # print(node_colors)
    # print_matrix(edge_matrix)
    for i in range(len(occup)):
        for j in range(len(occup)):
            if occup[i] == occup[j]:
                continue
            common_elements = set(occup[i]) & set(occup[j])
            if common_elements == set():
                continue
            shared = common_elements.pop()
            if shared == len(node_colors):
                continue
            a, b = occup[i]
            c, d = occup[j]

            if a == shared and b == shared:
                fr = shared
            else:
                for elm in occup[i]:
                    if elm != shared:
                        fr = elm

            if c == shared and d == shared:
                to = shared
            else:
                for elm in occup[j]:
                    if elm != shared:
                        to = elm


            move_color = edge_mapping.get((str(fr), str(to)), None)
            # print(str(fr), str(to),  move_color)
            if fr == len(node_colors):
                continue
            if move_color == None:
                # print("No edge from " + str(fr) + " to " + str(to) )
                continue

            node_color = node_colors[shared - 1]
            # print("Node " + str(shared) + ": " + node_color)

            if move_color != node_color:
                # print("The edge from " + str(fr) + " to " + str(to) + " is color " + move_color + " when it should be " + node_color)
                continue

            move_count += 1
            move_list.append([occup[i], occup[j]])
    # print("total valid moves = " + str(move_count))
    # print(move_list)
    return move_list

##ignoring 0, because all nodes start at 1
# def create_edge_matrix(dimensions, edge_list):
#     node_num = int(dimensions[0])
#     edge_color_matrix = []
#     for i in range(0, node_num):
#         row = []
#         for j in range(0, node_num):
#             row.append(0)
#         edge_color_matrix.append(row)
#     for edge in edge_list:
#         fr = int(edge[0])
#         to = int(edge[1])
#         color = edge[2]
#         edge_color_matrix[fr - 1][to - 1] = color
#
#     # print_matrix(edge_color_matrix)
#     return edge_color_matrix

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