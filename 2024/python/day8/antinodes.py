import argparse
from collections import defaultdict
from itertools import chain

def read_grid(file_path):
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file]
    return grid

def in_bounds(node, grid):
    """
    check x against columns, y against rows
    """
    return (-1 < node[0] < len(grid[0])) and (-1 < node[1] < len(grid))

def find_antinodes(network, grid):
    """
    calculate antinodes amongst a set of coordinates
    """
    antinodes = set()
    for loc1 in network:
        for loc2 in (network - set(loc1)):
            diff_x = loc1[0] - loc2[0]
            diff_y = loc1[1] - loc2[1]
            node1 = (loc1[0] + diff_x, loc1[1] + diff_y)
            node2 = (loc1[0] - diff_x, loc1[1] - diff_y)
            if in_bounds(node1, grid):
                antinodes.add(node1)
            if in_bounds(node2, grid):
                antinodes.add(node2)
    ans = antinodes - network
    if len(ans) < len(antinodes):
        print(f'removed {len(antinodes) - len(ans)} from antinodes ....')
    return ans

def find_collinear_points(network, grid):
    """
    calculate antinodes amongst a set of coordinates, where antinodes occur at any
    grid point collinear between any two network locations
    """
    antinodes = set()
    for loc1 in network:
        for loc2 in (network - set(loc1)):
            diff_x = loc1[0] - loc2[0]
            diff_y = loc1[1] - loc2[1]
            i = 1
            go_plus, go_minus = True, True
            while (go_plus and i < 48):
                node1 = (loc1[0] + i * diff_x, loc1[1] + i * diff_y)
                if in_bounds(node1, grid):
                    antinodes.add(node1)
                    i += 1
                else:
                    go_plus = False
            i = 1
            while(go_minus and i < 48):
                node2 = (loc1[0] - i * diff_x, loc1[1] - i * diff_y)    
                if in_bounds(node2, grid):
                    antinodes.add(node2)
                    i += 1
                else:
                    go_minus = False

    # apparently in Part 2 we consider antennae network locations as possible antinodes
    return antinodes


def PART_ONE(grid, debug=False):
    """
    count antinodes in grid of text
    """
    print(f'input grid is {len(grid)} rows and {len(grid[0])} columns')
    # build data structure of antenna frequencies
    antennae = defaultdict(set)     # frequency (char) -> locations { (x, y) }
    for y, row in enumerate(grid):
        for x, freq in enumerate(row):
            if freq != '.':
                antennae[freq].add((x, y))

    for k, v in antennae.items():
        print(f'{len(v)} antennae for the frequency {k}')

    # calculate antinodes (in-bounds) for each antenna set, store in list
    antinodes = []
    for network in antennae.values():
        antinodes.append(find_antinodes(network, grid))
    
    if debug:
        for grp in antinodes:
            print(f'antinode set: {str(grp)}')
    
    # flatten a list of sets into a single set
    uniq = set(chain.from_iterable(antinodes))
    
    if debug:
        for j, row in enumerate(grid):
            printrow = ['.' for x in row]
            for i, loc in enumerate(row):
                if (i, j) in uniq:
                    printrow[i] = '#'
                else:
                    printrow[i] = loc
            print(printrow)
    print()
    print(f'{len(uniq)} antinodes amongst all of these antenna pairs')

def PART_TWO(grid, debug=False):
    """
    count antinodes in grid of text, where each antinode occurs at every collinear point
    """
    # build data structure of antenna frequencies
    antennae = defaultdict(set)     # frequency (char) -> locations { (x, y) }
    for y, row in enumerate(grid):
        for x, freq in enumerate(row):
            if freq != '.':
                antennae[freq].add((x, y))

    # calculate antinodes (in-bounds) for each antenna set, store in list
    antinodes = []
    for network in antennae.values():
        antinodes.append(find_collinear_points(network, grid))
    # flatten a list of sets into a single set
    uniq = set(chain.from_iterable(antinodes))
    print()
    print(f'{len(uniq)} collinear-point antinodes amongst all of these antenna pairs')

if __name__ == '__main__':
    debug = False
    parser = argparse.ArgumentParser(description="Count antinodes in a grid of text.")
    parser.add_argument('file_path', help="Path to the text file containing the grid.")
    args = parser.parse_args()
    grid = read_grid(args.file_path)

    PART_ONE(grid, debug)
    PART_TWO(grid, True)