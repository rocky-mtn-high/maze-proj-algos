def gen_occupations(dimensions):
    node_num = int(dimensions[0])
    occupations = []

    for i in range(1, node_num + 1):
        for j in range(1, node_num + 1): ##change back to i+1
            occupations.append([i, j])
    # print(occupations)
    return occupations

def gen_moves(occup, edge_mapping, node_colors):
    move_count = 0
    move_list = []
    # print(node_colors)
    # print_matrix(edge_matrix)
    for i in range(len(occup)):
        for j in range(len(occup)):
            if occup[i] == occup[j]:
                continue
            # print(occup[i], occup[j])
            if occup[i][0] == occup[j][0]:
                shared = occup[i][0]
                fr = occup[i][1]
                to = occup[j][1]
                # print("shared: " + str(shared))
                # print("From/to: " + str(fr) + " " + str(to))

            elif occup[i][1] == occup[j][1]:
                shared = occup[i][1]
                fr = occup[i][0]
                to = occup[j][0]
            else:
                continue




            move_color = edge_mapping.get((str(fr), str(to)), None)
            # print(str(fr), str(to),  move_color)
            if fr == len(node_colors) + 1:
                continue
            if move_color == None:
                # print("No edge from " + str(fr) + " to " + str(to) )
                continue

            if shared == len(node_colors) + 1:
                continue
            node_color = node_colors[shared - 1]
            # print("Node " + str(shared) + ": " + node_color)


            if move_color != node_color:
                # print(shared)
                # print("The edge from " + str(fr) + " to " + str(to) + " is color " + move_color + " when it should be " + node_color)
                continue

            move_count += 1
            move_list.append([occup[i], occup[j]])
    # print("total valid moves = " + str(move_count))
    # print(move_list)
    return move_list

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