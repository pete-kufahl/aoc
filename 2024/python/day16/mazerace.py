import argparse
import heapq

def read_grid(file_path):
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file]
    return grid


def find_lowest_path(grid):
    """
    given a walled maze (obviating the in-bounds check), find the lowest-cost path
      to a goal E from start space S.
    each step foreward through '.' costs 1, each 90-deg rotation costs 1000.
    this is a classic weighted-path graph traversal --> use Dijkstra's algorithm
    - Dijkstra's requires a priority queue to store the path (put nodes of varying
       costs in, but always take the lowest-cost node out), which can be a heap.
    """
    # find starting point (see day 15)
    sr, sc = next(((rr, cc) for rr, row in enumerate(grid) for cc, loc in enumerate(row) if loc == 'S'), None)

    # priority queue stores tuple: (cost, row, col, row change, col change)
    #. note that the cost must be first element so that the heap algo sorts tuples by cost first
    #. start at S, facing the right
    pQueue = [(0, sr, sc, 0, 1)]
    # initialize set of "seen" locations, with facing direction
    seen = {(sr, sc, 0, 1)}
    while pQueue:
        # get the cheapest option off the queue
        cost, r, c, dr, dc = heapq.heappop(pQueue)
        seen.add((r, c, dr, dc))
        # check for end state
        if grid[r][c] == 'E':
            return cost

        # loop over 3 possible moves
        for new_cost, nr, nc, ndr, ndc in [(cost + 1, r + dr, c + dc, dr, dc),  # "forward" costs 1, direction unaffected
                                          (cost + 1000, r, c, dc, -dr),         # "clockwise": (row, col) --> (col, -row)
                                          (cost + 1000, r, c, -dc, dr)]:        # "counterclockwise" (row, col) --> (-col, row)
            if grid[nr][nc] == '#': continue        # wall
            if (nr, nc, ndr, ndc) in seen: continue # if seen this state (processing stage)
            # do not add --^ to seen: may not be the cheapest way to get to the state
            heapq.heappush(pQueue, (new_cost, nr, nc, ndr, ndc))

    return 0


def find_lowest_cost_and_path(grid):
    """
    returns both the lowest cost path to get through the maze, and all of the locations in that path.
    this requires an expansion of the Dijkstra's algorithm (above), in order to retain
      backtracking information.
    comments refer to additions/changes to find_lowest_path()
    """
    sr, sc = next(((rr, cc) for rr, row in enumerate(grid) for cc, loc in enumerate(row) if loc == 'S'), None)   
    pQueue = [(0, sr, sc, 0, 1)]

    # initialize lowest-cost path (as map of location->cost), backtrack set, and lowest cost
    lowest_cost_path = { (sr, sc, 0, 1): 0 }
    backtrack = {}
    best_cost = float('inf')
    end_states = set()
    
    while pQueue:
        # pop the cheapest option from queue
        cost, r, c, dr, dc = heapq.heappop(pQueue)

        # if the cost here is not the cheapest way to get to this location, skip
        if cost > lowest_cost_path.get((r, c, dr, dc), float('inf')): continue 

        # check for end state
        if grid[r][c] == 'E':
            if cost > best_cost: break              # no longer at cheapest way to E: end algo
            best_cost = cost
            end_states.add((r, c, dr, dc))

        for new_cost, nr, nc, ndr, ndc in [(cost + 1, r + dr, c + dc, dr, dc),
                                          (cost + 1000, r, c, dc, -dr),
                                          (cost + 1000, r, c, -dc, dr)]:
            if grid[nr][nc] == '#': continue

            # if we found the best way to get to (nr, nc) already, don't add this one
            lowest = lowest_cost_path.get((nr, nc, ndr, ndc), float('inf'))
            if new_cost > lowest: continue
            # otherwise, dump the backtrack
            if new_cost < lowest:
                backtrack[(nr, nc, ndr, ndc)] = set()
                lowest_cost_path[(nr, nc, ndr, ndc)] = new_cost
            # add previous location to the backtrack
            backtrack[(nr, nc, ndr, ndc)].add((r, c, dr, dc))

            heapq.heappush(pQueue, (new_cost, nr, nc, ndr, ndc))
    print(end_states)
    return lowest_cost_path, best_cost


def PART_ONE(grid, debug):
    if debug:
        for line in grid:
            print(*line, sep="")
    print(f'lowest-cost path through the maze: {find_lowest_path(grid)}')

def PART_TWO(grid, debug):
    path, cost = find_lowest_cost_and_path(grid)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="minimze cost of path through a maze")
    parser.add_argument('file_path', help="path to the text file containing maze")
    args = parser.parse_args()
    grid = read_grid(args.file_path)

    PART_ONE(grid, debug=False)
    print()
    PART_TWO(grid, debug=True)