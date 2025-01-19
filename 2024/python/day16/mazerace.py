import argparse

def read_grid(file_path):
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file]
    return grid

def PART_ONE(grid, debug):
    if debug:
        for line in grid:
            print(*line, sep="")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="minimze cost of path through a maze")
    parser.add_argument('file_path', help="path to the text file containing maze")
    args = parser.parse_args()
    grid = read_grid(args.file_path)

    PART_ONE(grid, debug=True)
    print()
    # PART_TWO(grid, debug=True)