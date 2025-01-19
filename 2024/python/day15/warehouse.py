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
    in the grid, the robot location is @
    in the robot string is its instructions:
     <, >, v, ^ are intended moves in that direction
     it will push any boxes (O) by one space if there's an empty space (.) to push to
     otherwise it is stopped by a wall (#)
    """
    pass


def PART_ONE(grid, robot, debug):
    if debug:
        for line in grid:
            print(line)
        print(robot)
    result_grid = track_robot(grid, robot, debug)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="track robot effects in warehouse")
    parser.add_argument('file_path', help="path to the text file containing warehouse layout and robot movements")
    args = parser.parse_args()
    grid, robot = parse_file(args.file_path)

    PART_ONE(grid, robot, debug=True)
    print()
    # PART_TWO(robots, rows=numrows, cols=numcols, debug=True)