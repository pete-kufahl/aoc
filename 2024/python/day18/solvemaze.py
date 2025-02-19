import argparse
from collections import deque

def read_grid_from_pairs(file_path, size, obstacles):
    grid = [[0] * size for _ in range(size)]

    with open(file_path, 'r') as file:
        coords = [list(map(int, line.split(","))) for line in file]
        for col, row in coords[:obstacles]:
            grid[row][col] = 1
    return grid, coords

def reset_grid(grid, size, coords):
    # Reset grid in place
    for row in range(size):
        for col in range(size):
            grid[row][col] = 0  # Set all cells to 0

    # Set specified coordinates to 1
    for col, row in coords:
        if 0 <= row < size and 0 <= col < size:  # Prevent IndexError
            grid[row][col] = 1



def find_shortest_path(grid, size) -> int:
    s = size - 1
    
    # breadth-frist search to find path from (0,0) to (size-1, size-1)
    # queue is row, col, distance; where distance is the number of steps from the start
    q = deque([(0, 0, 0)])
    seen = {(0, 0)}

    while q:
        r, c, d = q.popleft()
        for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if nr < 0 or nc < 0 or nr > s or nc > s:
                continue
            if grid[nr][nc] == 1:
                continue
            if (nr, nc) in seen:
                continue
            if nr == nc == s:
                return d + 1
            seen.add((nr, nc))
            q.append((nr, nc, d + 1))
    return -1

def PART_ONE(grid, size, debug):
    # find the shortest path through the maze
    if debug:
        for line in grid:
            print(*line, sep="")
    print(f'shortest path through the {size} x {size} maze: {find_shortest_path(grid, size)} steps')

def PART_TWO(grid, size, all_coords, debug):
    # find the first obstacle (X, Y) that makes the maze impossible to get through
    # this is basically a binary search through the sequence of possible obstacles,
    #.  given by all_coords

    lo, hi = 0, len(all_coords) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        reset_grid(grid, size, all_coords[:mid + 1])
        if find_shortest_path(grid, size) > -1:
            lo = mid + 1
        else:
            hi = mid
            
    print(f'first byte to render maze impassable is {all_coords[lo]}')
    

if __name__ == '__main__':
    # > python3 solvemaze.py input.txt 71 1024
    parser = argparse.ArgumentParser(description='minimize cost of path through a maze')
    parser.add_argument('file_path', help='path to the text file containing maze obstacles')
    parser.add_argument('size', help='number of rows/cols in the grid')
    parser.add_argument('obstacles', help='number of obstacles to be read from the file')
    args = parser.parse_args()
    size = int(args.size)
    obstacles = int(args.obstacles)
    grid, all_coords = read_grid_from_pairs(args.file_path, size, obstacles)

    PART_ONE(grid, size, debug=False)
    print()
    PART_TWO(grid, size, all_coords, debug=True)