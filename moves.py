
#create a dictionary where each node stores the other nodes it can possibly move to after checking color
def create_node_dictionary(nodes, edges):
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

    # print(mapping)
    return mapping

def create_moves(start, finish, dict):
    # print(start)
    # print(finish)
    move_ct = 0
    moves = []
    for key in dict:
        valid_from = dict[key]
        for fr in valid_from:
            moves.append([(int(key[0]), fr), (int(key[1]), fr)])
            moves.append([(fr, int(key[0])), (fr, int(key[1]))])
            move_ct += 2
    # print(move_ct)
    # print(moves)
    return moves




