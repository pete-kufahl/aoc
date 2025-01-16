import argparse
from collections import deque

def read_grid(file_path):
    """
    1. get contents of file into memory (char)
    2. convert all values in grid into integers
    """
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file]

    return grid

def in_bounds(r, c, grid):
    return (-1 < r < len(grid)) and (-1 < c < len(grid[0]))

def area(region):
    return len(region)

def perimeter(region):
    """
    find the perimeter of a connected region, made of a set of tuples
    """
    pass


def PART_ONE(grid, debug=False):
    """
    calculate fence boundaries in grid of text
    each region uses a fence that costs its area * its perimeter
    """
    rows = len(grid)
    cols = len(grid[0])
    print(f'input grid is {rows} rows and {cols} columns')
    
    regions = []
    visited = set()

    # visit all locations in farm just once
    for r in range(rows):
        for c in range(cols):
            if (r, c) in visited: continue
            visited.add((r, c))
            curr_region = set()
            curr_plant = grid[r][c]
            # now perform BFS to find all locations in current region
            # 1. initial queue has the starting point
            qBFS = deque[(r, c)]
            # 2. visit all neighbors
            while(qBFS):
                curr_r, curr_c = qBFS.popleft()
                # 2a. iterate through the directions to find neighboring (unseen) matching locations
                for next_r, next_c in [(curr_r-1, curr_c), (curr_r+1, curr_c), (curr_r, curr_c-1), (curr_r, curr_c+1)]:
                    if not in_bounds(next_r, next_c, grid): continue
                    if grid[next_r][next_c] != curr_plant: continue
                    if (next_r, next_c) in curr_region: continue
                    # 2b. add qualifying locations to the region and queue
                    curr_region.add((next_r, next_c))
                    qBFS.append((next_r, next_c))
            # 3. add region to the set of visited locations
            visited = visited | curr_region
            # 4. add region to the collection of regions
            regions.append(curr_region)






if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Calculate fence boundaries in a grid of text.")
    parser.add_argument('file_path', help="Path to the text file containing the grid.")
    args = parser.parse_args()
    grid = read_grid(args.file_path)

    PART_ONE(grid, True)
    # PART_TWO(grid, True)