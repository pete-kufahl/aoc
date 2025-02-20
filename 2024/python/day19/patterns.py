import argparse
from functools import cache

def parse_patterns_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
    patterns = set(lines[0].split(", "))    # separated by comma and space
    designs = lines[2:]
    return patterns, designs

@cache
def can_make_design(design, m) -> bool:
    # recursive function to match design from left to right
    # base case
    if design == "":
        return True
    # shorten the char-by-char searching a bit:
    for i in range(min(len(design), m) + 1):
        if design[:i] in patterns and can_make_design(design[i:], m):
            return True
    return False

@cache
def number_of_permutations(design, m) -> int:
    # modified recursion algorithm; instead of returning true/false,
    #. return the total number of ways the different patterns can make up the design
    # base case -> 1
    if design == "":
        return 1
    permuts = 0
    for i in range(min(len(design), m) + 1):
        if design[:i] in patterns:
            permuts += number_of_permutations(design[i:], m)
    return permuts

def PART_ONE(patterns, designs, debug=False):
    # figure out how many designs can be made with the patterns
    max_pattern_length = max(map(len, patterns))
    debug and print(f'maximum length of patterns = {max_pattern_length}')
    count = 0
    for design in designs:
        if can_make_design(design, max_pattern_length):
            count += 1
    print(f'{count} designs can be obtained from the {len(patterns)} patterns')


def PART_TWO(patterns, designs, debug=False):
    # add up how many different ways the designs can be made from the patterns
    max_pattern_length = max(map(len, patterns))
    count = 0
    for design in designs:
        count += number_of_permutations(design, max_pattern_length)
    print(f'{count} total permutations can be obtained from the {len(designs)} designs')

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Optimize claw-machine movements defined in text.")
    parser.add_argument('file_path', help="Path to the text file containing claw-machine problems.")
    args = parser.parse_args()
    patterns, designs = parse_patterns_file(args.file_path)

    PART_ONE(patterns, designs, True)
    print()
    PART_TWO(patterns, designs, False)