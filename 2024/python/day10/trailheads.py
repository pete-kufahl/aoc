import argparse

def read_grid(file_path):
    """
    1. get contents of file into memory (char)
    2. convert all values in grid into integers
    """
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file]

    intGrid = [[int(char) for char in row] for row in grid]
    return intGrid

def get_starting_points(grid, start_digit: int = 0):
    """
    return list of all (row, col) coordinates in the grid where the value is 0
    """
    startPoints = [(ridx, cidx)
                   for ridx, row in enumerate(grid)
                   for cidx, val in enumerate(row)
                   if val == start_digit]
    return startPoints
    
def in_bounds(node, grid):
    """
    check x against columns, y against rows
    """
    return (-1 < node[0] < len(grid[0])) and (-1 < node[1] < len(grid))

def PART_ONE(grid, debug=False):
    """
    count antinodes in grid of text
    """
    print(f'input grid is {len(grid)} rows and {len(grid[0])} columns')

if __name__ == '__main__':
    debug = False
    parser = argparse.ArgumentParser(description="Count antinodes in a grid of text.")
    parser.add_argument('file_path', help="Path to the text file containing the grid.")
    args = parser.parse_args()
    grid = read_grid(args.file_path)

    PART_ONE(grid, debug)
    # PART_TWO(grid, True)