import argparse

def get_input(file_path):
    locks = []
    keys = []
    with open(file_path, 'r') as file:
        for block in file.read().split("\n\n"):
            # convert block of rows to column data
            grid = list(zip(*block.splitlines()))
            if grid[0][0] == "#":
                # convert to the pin-height for each column, store as lock
                locks.append([row.count("#") - 1 for row in grid])
            else:
                keys.append([row.count("#") - 1 for row in grid])
    return locks, keys


def PART_ONE(locks, keys, debug=False):
    if debug:
        print(*locks)
        print(*keys)
    # check every combination for no-overlap case
    total = 0
    for lock in locks:
        for key in keys:
            # compare the corresponding column values
            if all(x + y <= 5 for x, y in zip(lock, key)):
                total += 1
    print(f'there are {total} combinations of locks and keys without overlapping pins')


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="find pairs of keys and locks that fit")
    parser.add_argument('file_path', help="path to the text file containing the schematics")
    args = parser.parse_args()
    locks, keys = get_input(args.file_path)
    PART_ONE(locks, keys, False)