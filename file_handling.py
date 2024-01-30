import sys
import fileinput


def file_import():
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_input_file>")
        sys.exit(1)

    input_file_path = sys.argv[1]

    try:
        # Use fileinput.input() to handle both stdin and file input
        input_lines = []
        with fileinput.input(files=(input_file_path,)) as f:
            for line in f:
                input_lines.append(line)
            return process_input(input_lines)
    except FileNotFoundError:
        print(f"Error: File '{input_file_path}' not found.")
        sys.exit(1)

def test_import():
    with open("./test0.txt", "r") as file:
        input_lines = []
        for line in file:
            input_lines.append(line)
        return process_input(input_lines)
    return 0

def process_input(input_lines):
    dimensions = input_lines[0].split()
    node_colors = input_lines[1].split()
    start_positions = input_lines[2].split()
    edges = []
    for i in range(3, len(input_lines)):
        edges.append(input_lines[i].split())

    # print("dimensions: " + dimensions[0]  + " " + dimensions[1])
    # print("node colors: " + node_colors[0])
    # print("start positions: " + start_positions[0] + " " +  start_positions[1])
    # print(edges[1])

    return dimensions, node_colors, start_positions, edges