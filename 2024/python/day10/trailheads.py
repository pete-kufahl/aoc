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
    
def is_valid(x, y, grid, prev):
    """
    check x against columns, y against rows, value against previous value (prev)
    """
    return (0 <= x < len(grid)) and (0 <= y < len(grid[0])) and (grid[x][y] == prev + 1)

def PART_ONE(grid, debug=False):
    """
    find 0..9 paths in grid of integers
    """
    print(f'input grid is {len(grid)} rows and {len(grid[0])} columns')
    starts = get_starting_points(grid, 0)
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)] # down, right, up, left
    solutions = []

    def dfs(x, y, path, summits):
        """
        inner recursive depth-first search to find the paths
        """
        path.append((x, y))
        if grid[x][y] == 9:
            # stop recursion, store copy of path (if summit not reached before)
            if (x, y) not in summits:
                summits.append((x, y))
                solutions.append(path[:])
        else:
            for dx, dy in directions:
                newx, newy = x + dx, y + dy
                if is_valid(newx, newy, grid, grid[x][y]):
                    dfs(newx, newy, path, summits)
        path.pop()  # backtrack

    total_score = 0
    for sx, sy in starts:
        dfs(sx, sy, [], [])
        print(f'starting point ({sx}, {sy}) has score {len(solutions)}')
        total_score += len(solutions)
        debug and print(solutions)
        solutions = []
    print(f'total score for grid is {total_score}')
    

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Count antinodes in a grid of text.")
    parser.add_argument('file_path', help="Path to the text file containing the grid.")
    args = parser.parse_args()
    grid = read_grid(args.file_path)

    PART_ONE(grid, False)
    # PART_TWO(grid, True)