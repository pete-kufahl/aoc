import argparse
from collections import deque

def read_grid(file_path):
    """
    get contents of file into memory (char)
    """
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file]
    return grid


def inbounds(r, c, grid) -> bool:
    rows = len(grid)
    cols = len(grid[0])
    if (r < 0) or (c < 0) or (r >= rows) or (c >= cols):
        return False
    return True


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


def edges(region):
    """
    find the number of edges in the shape defined by the coordinates of a region
    """
    pass


def connected_regions(grid):
    """
    use breadth-first search to visit every location in the grid and group them into
    regions of common plants. Returns a list of sets, where each element in each set
    is a (row, col) tuple corresponding to a location in the grid.
    """
    regions = []
    rows = len(grid)
    cols = len(grid[0])
    visited = set()

    # visit all locations in farm just once
    for r in range(rows):
        for c in range(cols):
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
                    # 2b. add qualifying locations to the region and queue
                    #   compare numbers, then two chars, then tuples
                    if inbounds(next_r, next_c, grid) and (grid[next_r][next_c] == curr_plant) and ((next_r, next_c) not in curr_region):
                        curr_region.add((next_r, next_c))
                        qBFS.append((next_r, next_c))
            # 3. add region to the set of visited locations
            visited = visited | curr_region
            # 4. add region to the collection of regions
            regions.append(curr_region)
    return regions

def PART_ONE(grid, debug=False):
    """
    calculate fence boundaries in grid of text
    each region uses a fence that costs its area * its perimeter
    """    
    regions = connected_regions(grid)

    if debug:
        locs = sum(len(region) for region in regions)
        print(f'{locs} locations accounted for in grid of {len(grid) * len(grid[0])} cells')
        for region in regions:
            print(f'area: {area(region)}, perimeter: {perimeter(region)}')

    fences = sum(area(region) * perimeter(region) for region in regions)
    print(f'total fence units is {fences} for {len(regions)} regions')


def PART_TWO(grid, debug=False):
    """
    calculate fence boundaries in grid of text
    each region uses a fence that costs its area * its number of edges
    """
    regions = connected_regions(grid)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Calculate fence boundaries in a grid of text.")
    parser.add_argument('file_path', help="Path to the text file containing the grid.")
    args = parser.parse_args()
    grid = read_grid(args.file_path)

    PART_ONE(grid, False)
    PART_TWO(grid, True)