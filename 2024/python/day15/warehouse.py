import argparse

def parse_file(file_path):
    grid = None
    robot = None
    with open(file_path, 'r') as file:
        # input is split by 2 newlines
        top, bot = file.read().split('\n\n')
        grid = [list(line) for line in top.splitlines()]
        robot = bot.replace("\n", "")
    return grid, robot

def track_robot(grid, robot, debug):
    """
    * grid is surround by wall (#) -> no need for an in-bounds check
    * robot param is a series of moves
     it will push any boxes (O) by one space if there's an empty space (.) to push to
     otherwise it is stopped by a wall (#)
    """
    # find starting point (@), tbh a nested for ... else loop would also make sense
    r, c = next(((rr, cc)
                for rr, row in enumerate(grid)
                for cc, loc in enumerate(row)
                if loc == '@'), None)
    debug and print (r, c)

    # identify and register effects of robot movements
    for move in robot:
        # <, >, v, ^ are intended moves in that direction
        delr = { '^': -1, 'v': 1 }.get(move, 0)
        delc = { '<': -1, '>': 1 }.get(move, 0)
        
        targets = [(r,c)]       # intended move targets, starting with the robot position
        curr_r, curr_c = r, c   # location we are looking at
        can_move = True         # whether the move happens 
        while True:
            curr_r += delr
            curr_c += delc
            loc = grid[curr_r][curr_c]
            if loc == '#':      # there's a wall in the way
                can_move = False
                break
            if loc == 'O':      # a box to move, maybe
                targets.append((curr_r, curr_c))
            if loc == '.':      # open space -> commence moving
                break
        if can_move:
            # robot, and any boxes in front of it, move by one space
            debug and print(f'moving ({move}) robot to ({r + delr}, {c + delc}) with {len(targets) - 1} boxes')
            grid[r][c] = '.'                # robot vacates position
            grid[r + delr][c + delc] = '@'  # robot's new location
            for box_r, box_c in targets[1:]:
                grid[box_r + delr][box_c + delc] = 'O'
            r += delr
            c += delc
    
    if debug:
        for row in grid:
            print(*row, sep="")
    return grid

def score_grid(grid):
    """
    use generator expression
    sum the score for each box at (row, col): 100 * row + 1 * col
    """
    rows = len(grid)
    cols = len(grid[0])
    return sum(100 * r + c 
               for r in range(rows) 
               for c in range(cols)
               if grid[r][c] == 'O')

def PART_ONE(grid, robot, debug):
    if debug:
        for line in grid:
            print(line)
        print(robot)
    result_grid = track_robot(grid, robot, debug)
    print(f'final GPS score = {score_grid(result_grid)}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="track robot effects in warehouse")
    parser.add_argument('file_path', help="path to the text file containing warehouse layout and robot movements")
    args = parser.parse_args()
    grid, robot = parse_file(args.file_path)

    PART_ONE(grid, robot, debug=True)
    print()
    # PART_TWO(robots, rows=numrows, cols=numcols, debug=True)