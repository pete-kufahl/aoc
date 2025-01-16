import argparse

def read_grid(file_path):
    """
    1. get contents of file into memory (char)
    2. convert all values in grid into integers
    """
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file]

    return grid

def in_bounds(node, grid):
    """
    check x against columns, y against rows
    """
    return (-1 < node[0] < len(grid[0])) and (-1 < node[1] < len(grid))

def PART_ONE(grid, debug=False):
    """
    calculate fence boundaries in grid of text
    each region uses a fence that costs its area * its perimeter
    """
    print(f'input grid is {len(grid)} rows and {len(grid[0])} columns')

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Calculate fence boundaries in a grid of text.")
    parser.add_argument('file_path', help="Path to the text file containing the grid.")
    args = parser.parse_args()
    grid = read_grid(args.file_path)

    PART_ONE(grid, True)
    # PART_TWO(grid, True)