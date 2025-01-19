import argparse
import re

def parse_robot_file(file_path):
    """
    use regular express to find positive and negative numbers in every line,
    convert them into signed integers and package them into tuples
    """
    robots = []

    with open(file_path, 'r') as file:
        for line in file:
            nums = tuple(map(int, re.findall(r"-?\d+", line)))
            robots.append(nums)
    print(robots)



def PART_ONE(robots, rows, cols, debug=False):
    pass


if __name__ == '__main__':
    # > python3 robots.py example.txt 11 7
    parser = argparse.ArgumentParser(description="Track robot movements on a grid.")
    parser.add_argument('file_path', help="Path to the text file containing robot positions and velocities.")
    parser.add_argument('rows', help='number of rows in the grid (height)')
    parser.add_argument('cols', help='number of columns in the grid (width)')
    args = parser.parse_args()
    robots = parse_robot_file(args.file_path)
    numrows = int(args.rows)
    numcols = int(args.cols)

    PART_ONE(robots, rows=numrows, cols=numcols, debug=False)
    print()
    # PART_TWO(problems, False)