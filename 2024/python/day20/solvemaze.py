import argparse
from collections import deque

def read_grid(file_path):
    """
    get contents of file into memory (char)
    """
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file]
    return grid


def solve_grid(grid, amount, debug=False) -> int:
    rows, cols, dists = grid_of_distances(grid, debug)
    
    # use the grid of distances to evaluate the possible "cheats"
    #. we want to find the number of cheats that save a net 102 on distance
    #. (it costs to 2 to make the jump)
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '#': continue  # or, if the dist here == -1
            # evaluate cheat directions (4 ways)
            # .............. down ...down/right .. right .. up/right
            for nr, nc in [(r+2, c), (r+1, c+1), (r, c+2), (r-1, c+1)]:
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                    continue
                if grid[nr][nc] == '#':
                    continue
                # using abs() here means looping thru only 4 cheat directions instead of 8
                if abs(dists[r][c] - dists[nr][nc]) >= (amount+2):
                    count += 1
    return count

def solve_grid_with_radius(grid, amount, cheatsize, debug=False) -> int:
    # search through the grid of distances, this time evaluate jumps of up
    #. to the given cheatsize (incl.)
    rows, cols, dists = grid_of_distances(grid, debug)
    count = 0
    for r in range(rows):
        for c in range(cols):
            # evaluate jumps of size 2 up to the cheatsize -> radius
            for radius in range(2, cheatsize + 1):
                # for a given radius, the possible jumps are along a diamond
                #.  deltas: dr + dc = radius
                for dr in range(radius + 1):
                    dc = radius - dr
                    # loop over a set of directions (avoid retesting points when dr or dc = 0)
                    for nr, nc in {(r + dr, c + dc), (r + dr, c - dc), (r - dr, c + dc), (r - dr, c - dc)}:
                        if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                            continue
                        if grid[nr][nc] == '#':
                            continue
                        # testing in all directions --> signed comparison
                        if dists[r][c] - dists[nr][nc] >= (amount + radius):
                            count += 1
    return count

def grid_of_distances(grid, debug):
    # helper function that calculates, by BFS, all the distances along the path to 
    #. the ending position, from the starting position
    rows = len(grid)
    cols = len(grid[0])

    # find start position at r, c; use for .. else .. break syntax
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                break
        else:
            continue
        break
    
    # BFS to fill
    # use a grid to find the distance to every point from the start
    #. -1 --> not reached that position yet
    dists = [[-1] * cols for _ in range(rows)]
    dists[r][c] = 0

    # positions that known to be reachable, but have not been "explored" yet (i.e. visited their neighbors) 
    q = deque([(r, c)])
    # continue while we have open nodes to explore
    while q:
        cr, cc = q.popleft()
        for nr, nc in [(cr+1, cc), (cr-1, cc), (cr, cc+1), (cr, cc-1)]:
            if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                continue
            if grid[nr][nc] == '#':
                continue
            # BFS --> if we see a node for a second time, we've already found the nearest
            #. path to it, so skip it this time
            if dists[nr][nc] != -1:
                continue
            dists[nr][nc] = dists[cr][cc] + 1
            q.append((nr, nc))
    
    # the grid of distances
    if debug:
        for row in dists:
            print(*row, sep='\t')

    return rows,cols,dists


def PART_ONE(grid, amount=100, debug=False):
    cheats = solve_grid(grid, amount, debug)
    print(f'in the maze, found {cheats} jumps that would save {amount} ps')


def PART_TWO(grid, amount=100, cheatsize=20, debug=False):
    cheats = solve_grid_with_radius(grid, amount, cheatsize, debug)
    print(f'in the maze, found {cheats} jumps up to size {cheatsize} that would save {amount} ps')


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="find shortcuts in a maze of text characters")
    parser.add_argument('file_path', help="Path to the text file containing the grid.")
    parser.add_argument('amount', default=100, help="Amount to time (ps) saved by qualifying cheats.")
    parser.add_argument('cheat_size', default=20, help='maximum cost of a cheat (ps)')
    args = parser.parse_args()
    grid = read_grid(args.file_path)
    amount = int(args.amount)
    cheatsize = int(args.cheat_size)

    PART_ONE(grid, amount, False)
    print()
    PART_TWO(grid, amount, cheatsize, False)