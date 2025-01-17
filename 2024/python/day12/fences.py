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


def sides(grid, region, debug=True):
    """
    find the number of sides around the shape defined by the coordinates of a region. 
    do this by finding the border edge of each location, and which direction 
    it's outwardly facing.
    then adjacent edges facing the same direction cancel each other, leaving
      a count of the continuous edges of the region, a.k.a. the sides.
    """
    # store the oriented edges as a map (r, c) => outwardly direction
    edges = {}
    # iterate through every direction of every location
    for curr_r, curr_c in region:
        for next_r, next_c in [(curr_r-1, curr_c), (curr_r+1, curr_c), (curr_r, curr_c-1), (curr_r, curr_c+1)]:
            if (next_r, next_c) not in region:
                # each edge stored as the average x-, y-coordinate of the locations it separates
                edge_r = (curr_r + next_r) / 2
                edge_c = (curr_c + next_c) / 2
                # the direction is the edges coordinates relative to the curr_r, curr_c location (i.e., origin)
                edges[(edge_r, edge_c)] = (edge_r - curr_r, edge_c - curr_c)
    if debug:
        print("--" * 30)
        r, c = list(region)[0]
        print(grid[r][c], ': ')
        print(edges)

    # consolidate edges: for each edge in the map, eliminate (from the running count of sides) 
    #  every adjacent edge that has the same whole-number
    #  coordinate and direction (thus keeping kitty-corner edges along the same 
    #  line but facing opposite directions)
    # traverse the map keys and visit neighbors
    visited = set()
    num_sides = 0
    for edge, direction in edges.items():
        if edge not in visited:
            visited.add(edge)
            num_sides += 1
            edge_r, edge_c = edge
            # edge on the left/right => visit up/down
            if edge_r % 1 == 0:
                for delta_r in [-1, 1]:
                    next_r = edge_r + delta_r
                    # check presence and direction of edge on next row over
                    while edges.get((next_r, edge_c)) == direction:
                        visited.add((next_r, edge_c))
                        next_r += delta_r
            else:
                # edge on the top/bottom => visit left/right
                for delta_c in [-1, 1]:
                    next_c = edge_c + delta_c
                    # check presence and direction of edge on next column over
                    while edges.get((edge_r, next_c)) == direction:
                        visited.add((edge_r, next_c))
                        next_c += delta_c
    return num_sides


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
    print(f'1.) total fence units is {fences} for {len(regions)} regions')


def PART_TWO(grid, debug=False):
    """
    calculate fence boundaries in grid of text
    each region uses a fence that costs its area * its number of edges
    """
    regions = connected_regions(grid)
    fences = sum(area(region) * sides(grid, region, debug) for region in regions)
    print(f'2.) total fence units is {fences} for {len(regions)} regions')


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Calculate fence boundaries in a grid of text.")
    parser.add_argument('file_path', help="Path to the text file containing the grid.")
    args = parser.parse_args()
    grid = read_grid(args.file_path)

    PART_ONE(grid, False)
    print()
    PART_TWO(grid, False)