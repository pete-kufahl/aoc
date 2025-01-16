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
    each location in the set has a perimeter of 4,
    but for every shared edge with another location, substract that locations perimeter by 1
    """
    total_perimeter = 0
    for curr_r, curr_c in region:
        total_perimeter += 4
        for next_r, next_c in [(curr_r-1, curr_c), (curr_r+1, curr_c), (curr_r, curr_c-1), (curr_r, curr_c+1)]:
            if (next_r, next_c) in region:
                total_perimeter -= 1

    return total_perimeter


def PART_ONE(grid, debug=False):
    """
    calculate fence boundaries in grid of text
    each region uses a fence that costs its area * its perimeter
    """
    rows = len(grid)
    cols = len(grid[0])
    debug and print(f'input grid is {rows} rows and {cols} columns')
    
    regions = []
    visited = set()

    # visit all locations in farm just once
    for r in range(rows):
        for c in range(cols):
            # start_pt = (r, c)
            if (r, c) in visited: continue
            visited.add((r, c))
            curr_region = {(r, c)}
            curr_plant = grid[r][c]

            # now perform BFS to find all locations in current region
            # 1. initial queue has the starting point
            qBFS = deque([(r, c)])
            # 2. visit all neighbors
            while qBFS:
                curr_r, curr_c = qBFS.popleft()
                # 2a. iterate through the directions to find neighboring (unseen) matching locations
                for next_r, next_c in [(curr_r-1, curr_c), (curr_r+1, curr_c), (curr_r, curr_c-1), (curr_r, curr_c+1)]:
                    # if not in_bounds(next_r, next_c, grid): continue
                    if next_r < 0 or next_c < 0 or next_r >= rows or next_c >= cols: continue
                    if grid[next_r][next_c] != curr_plant: continue
                    if (next_r, next_c) in curr_region: continue
                    # 2b. add qualifying locations to the region and queue
                    curr_region.add((next_r, next_c))
                    qBFS.append((next_r, next_c))
            # 3. add region to the set of visited locations
            visited = visited | curr_region
            # 4. add region to the collection of regions
            regions.append(curr_region)
    

    if debug:
        for region in regions:
            print(f'area: {area(region)}, perimeter: {perimeter(region)}')

    fences = sum(area(region) * perimeter(region) for region in regions)
    print(f'total fence units is {fences} for {len(regions)} regions')


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Calculate fence boundaries in a grid of text.")
    parser.add_argument('file_path', help="Path to the text file containing the grid.")
    args = parser.parse_args()
    grid = read_grid(args.file_path)

    PART_ONE(grid, True)
    # PART_TWO(grid, True)