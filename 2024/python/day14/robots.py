import argparse
import re
import math

def parse_robot_file(file_path):
    """
    use regular expression to find positive and negative numbers in every line,
    convert them into signed integers and package them into a tuple
    """
    robots = []

    with open(file_path, 'r') as file:
        for line in file:
            nums = tuple(map(int, re.findall(r"-?\d+", line)))
            robots.append(nums)
    return robots

def simulate(robots, height, width, iters=100):
    """
    simulate robot movements in a wrap-around arena (no need to store a grid)
    no need to do a loop, since robot/robot interactions do not matter and
      we just use modulo to see where they end up
    """
    results = []    # (x, y) tuples

    # sample row of data: p=0,4 v=3,-3
    for px, py, vx, vy in robots:
        results.append(((px + vx * iters) % width, (py + vy * iters) % height))
    return results

def calc_safety_factor(bots, height, width):
    """
    count the number of robots in each quadrant of the grid (defined by width * height),
    multiply these counts together
    """
    # the robots in the median row/col do not count
    vert_median = (height-1) // 2
    horiz_median = (width-1) // 2
    quads = [0] * 4

    for rx, ry in bots:
        if rx == horiz_median or ry == vert_median:
            continue
        # assign robot to quadrant
        if rx < horiz_median:
            if ry < vert_median:
                quads[0] += 1       # top left
            else:
                quads[1] += 1       # bottom left
        elif ry < vert_median:
            quads[2] += 1           # top right
        else:
            quads[3] += 1           # bottom right

    return math.prod(quads)    # python 3.8


def PART_ONE(robots, rows, cols, debug=False):
    # we're always given an odd number of rows and cols; modify calc_safety_factor if this isn't true
    height = rows
    width = cols
    iters = 100
    if debug:
        print(robots)
    moved_robots = simulate(robots, height=height, width=width, iters=iters)
    safety_factor = calc_safety_factor(bots=moved_robots, height=height, width=width)
    print(f'safety factor after {iters} iterations: {safety_factor}')

    
if __name__ == '__main__':
    # > python3 robots.py example.txt 11 7
    # > python3 robots.py input.txt 103 101
    parser = argparse.ArgumentParser(description="Track robot movements on a grid.")
    parser.add_argument('file_path', help="Path to the text file containing robot positions and velocities.")
    parser.add_argument('rows', help='number of rows in the grid (height)')
    parser.add_argument('cols', help='number of columns in the grid (width)')
    args = parser.parse_args()
    robots = parse_robot_file(args.file_path)
    numrows = int(args.rows)
    numcols = int(args.cols)

    PART_ONE(robots, rows=numrows, cols=numcols, debug=False)
    print()
    # PART_TWO(problems, False)