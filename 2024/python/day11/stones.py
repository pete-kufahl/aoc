import argparse
from collections import defaultdict

def blink(stoneCounts):
    """
    iterate the collection of stones (their order does not matter)
    1. "0" --> "1"
    2. even number of digits --> 2 stones, one with the left half and the other with the right half
    3. otherwise, x --> 2024 * x
    """
    nextStoneCounts = defaultdict(int)

    # the number x is engraved on a given stone
    for x in stoneCounts:
        if x == 0:
            nextStoneCounts[1] += stoneCounts[x]
        elif len(str(x)) % 2 == 0:
            x_str = str(x)
            center = len(x_str) // 2
            # integer casting takes out the leading zeroes, as instructed
            nextStoneCounts[ int(x_str[center:]) ] += stoneCounts[x]    # left side
            nextStoneCounts[ int(x_str[:center]) ] += stoneCounts[x]    # right side
        else:
            nextStoneCounts[ x * 2024 ] += stoneCounts[x]
    
    return nextStoneCounts
			


def PART_ONE_OR_TWO(initial_stones, blinks: int = 25, debug: bool = False):
    """
    count how many stones are in a row, after 25 *blinks*
    the order of the stones does not matter, so store in dict (number of stone --> number of stones) to save space
    """
    stoneCounts = defaultdict(int)      # match type in blink()
    for stone in set(initial_stones):
        stoneCounts[stone] = initial_stones.count(stone)

    for i in range(blinks):
        # replace the row of stones with a new row
        stoneCounts = blink(stoneCounts)
        if debug and i < 6:
            print (f'***** {i} *****')
            print(stoneCounts)

    # generator expr. for summing the dict values
    total = sum(val for val in stoneCounts.values())
    print(f'after {blinks} blinks, {total} stones in the row')
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Count stones after a number of iterations.")
    parser.add_argument('file_path', help="Path to the text file with one line of stones.")
    args = parser.parse_args()
    initial_stones = []

    # read one line 
    with open(args.file_path) as f:
        initial_stones = [int(x) for x in f.read().strip().split()]

    if initial_stones:
        PART_ONE_OR_TWO(initial_stones, 25, False)
        PART_ONE_OR_TWO(initial_stones, 75, False)


