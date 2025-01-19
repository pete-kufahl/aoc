import argparse
import re

def parse_robot_file(filepath):
    pass


def PART_ONE(robots, rows, cols, debug=False):
    pass


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Track robot movements on a grid.")
    parser.add_argument('file_path', help="Path to the text file containing robot positions and velocities.")
    parser.add_argument('rows', help='number of rows in the grid')
    parser.add_argument('cols', help='number of columns in the grid')
    args = parser.parse_args()
    robots = parse_robot_file(args.file_path)
    numrows = int(args.rows)
    numcols = int(args.cols)

    PART_ONE(robots, rows=numrows, cols=numcols, debug=False)
    print()
    # PART_TWO(problems, False)