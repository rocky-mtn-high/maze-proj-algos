def gen_occupations(dimensions):
    node_num = int(dimensions[0])
    occupations = []

    for i in range(1, node_num + 1):
        for j in range(i, node_num + 1): ##change back to i+1
            occupations.append([i, j])
    # print(occupations)
    return occupations

def gen_moves(occup, edge_matrix, node_colors):
    move_count = 0
    move_list = []
    node_colors.append('finish')
    # print(node_colors)
    # print_matrix(edge_matrix)
    for i in range(len(occup)):
        for j in range(len(occup)):
            if i == j:
                continue

            ##The different positions must have exactly one similar node between them
            common_elements = set(occup[i]) & set(occup[j])
            if len(common_elements) != 1:
                # print(str(occup[i]) + " " + str(occup[j]) + " disqualified because they have no common elements.")
                continue
            shared = common_elements.pop()

            # The different nodes between the occupations must have an edge between them.
            # i.e., matrix[a][b] must be nonzero because this is a directed graph.
            origin = 0
            final = 0
            if occup[i][0] == occup[i][1]:
                origin = occup[i][0]
            elif occup[j][0] == occup[j][1]:
                final = occup[j][0]
            else:
                origin = next(node for node in occup[i] if node != shared)
                final = next(node for node in occup[j] if node != shared)
            move_color = edge_matrix[origin -1 ][final - 1 ]
            if move_color == 0:
                # print(str(occup[i]) + " " + str(occup[j]) + " disqualified because there is no directed edge between the changed nodes.")
                continue
            # print("for " + str(occup[i]) + " and " + str(occup[j]) + " the change is " + str(origin) + " --> " + str(final))

            # The shared node between occupations must be of the same color as the edge that exists.
            shared_color = node_colors[shared - 1]  # must be -1
            # print(str(shared) + " color: " + shared_color)
            if str(move_color) != str(shared_color) and shared_color != 'finish':
                # print(str(occup[i]) + " " + str(occup[j]) + " disqualified because the edge is the wrong color.")
                # print("The edge is " + str(move_color) + ", whereas the node is " + str(shared_color))
                continue
            move_count += 1
            move_list.append([occup[i], occup[j]])
    # print("total valid moves = " + str(move_count))
    # print(move_list)
    return move_list

##ignoring 0, because all nodes start at 1
def create_edge_matrix(dimensions, edge_list):
    node_num = int(dimensions[0])
    edge_color_matrix = []
    for i in range(0, node_num + 1):
        row = []
        for j in range(0, node_num + 1):
            row.append(0)
        edge_color_matrix.append(row)
    for edge in edge_list:
        fr = int(edge[0])
        to = int(edge[1])
        color = edge[2]
        edge_color_matrix[fr - 1][to - 1] = color

    # print_matrix(edge_color_matrix)
    return edge_color_matrix


def print_matrix(matrix):
    for row in matrix:
        r = ""
        for elm in row:
            r = r + str(elm)
        print(r)
    return 0