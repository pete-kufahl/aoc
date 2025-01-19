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

def track_robot_small_boxes(grid, robot, debug):
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

def score_grid(grid, box='O'):
    """
    use generator expression
    sum the score for each box at (row, col): 100 * row + 1 * col
    """
    rows = len(grid)
    cols = len(grid[0])
    return sum(100 * r + c 
               for r in range(rows) 
               for c in range(cols)
               if grid[r][c] == box)


def expand_grid(grid):
    """
    make grid twice as wide (except for robot)
    """
    expand = {
        '#': '##',
        '.': '..',
        'O': '[]',
        '@': '@.'
    }
    result = []
    for row in grid:
        wide_str = ''.join(expand[char] for char in row)
        result.append(list(wide_str))
    return result


def track_robot_wide_boxes(grid, robot, debug):
    """
    alter the algo for tracking the robot in the small warehouse, because we have to
      handle multiple coordinates at once.
    the robot can move multiple boxes forward (even if they line up halfway), if there's
      no wall to stop them; that means we add box-halves ([,]) to the targets when we
      encounter them, an only move if there's open space in front of all the targets.
    """
    # starting position of robot, same as before
    r, c = next(((rr, cc) for rr, row in enumerate(grid) for cc, loc in enumerate(row) if loc == '@'), None)

    for move in robot:
        # <, >, v, ^ are intended moves in that direction
        delr = { '^': -1, 'v': 1 }.get(move, 0)
        delc = { '<': -1, '>': 1 }.get(move, 0)

        targets = [(r,c)]       # intended move targets, starting with the robot position
        can_move = True         # whether the move happens 

        # find all the targets for this move
        # iterate through targets, adding to it when [] enountered.
        #.  note: not the safest thing to do, can only do with list
        for tr, tc in targets:
            nr = tr + delr
            nc = tc + delc
            if (nr, nc) in targets: continue    # avoid double-add
            loc = grid[nr][nc]
            if loc == '#':      # there's a wall in the way
                can_move = False
                break
            if loc == '[':      # left half of box
                targets.append((nr, nc))
                targets.append((nr, nc + 1))
            if loc == ']':      # right half of box
                targets.append((nr, nc))
                targets.append((nr, nc - 1))
            # no need for '.' check, as all targets must end before a wall
            #. for can_move to remain True
        if can_move:
            # make a deep copy of the grid, to modify grid with previous version on the right side
            prevgrid = [list(row) for row in grid]
            # robot, and any boxes in front of it, move by one space
            debug and print(f'moving ({move}) robot to ({r + delr}, {c + delc}) with {len(targets) - 1} boxes')
            grid[r][c] = '.'                # robot vacates position
            grid[r + delr][c + delc] = '@'  # robot's new location
            for box_r, box_c in targets[1:]:    # 1. target positions set to .
                grid[box_r][box_c] = '.'
            for box_r, box_c in targets[1:]:    # 2. override those . with moved-to targets
                grid[box_r + delr][box_c + delc] = prevgrid[box_r][box_c]
            r += delr
            c += delc         
    if debug:
        for row in grid:
            print(*row, sep="")
    return grid    


def PART_ONE(grid, robot, debug):
    if debug:
        for line in grid:
            print(line)
        print(robot)
    result_grid = track_robot_small_boxes(grid, robot, debug)
    score = score_grid(result_grid)
    print(f'final GPS score (small boxes) = {score}')


def PART_TWO(grid, robot, debug):
    """
    when computing the score, the [ side of the box is closest to the left edge
    """
    wide_grid = expand_grid(grid)
    if debug:
        for line in wide_grid:
            print(line)
        print(robot)
    result_grid = track_robot_wide_boxes(wide_grid, robot, debug)
    score = score_grid(result_grid, '[')
    print(f'final GPS score (wide boxes) = {score}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="track robot effects in warehouse")
    parser.add_argument('file_path', help="path to the text file containing warehouse layout and robot movements")
    args = parser.parse_args()
    grid, robot = parse_file(args.file_path)

    PART_ONE(grid, robot, debug=False)
    print()

    # reset grid
    grid, robot = parse_file(args.file_path)
    PART_TWO(grid, robot, debug=True)
