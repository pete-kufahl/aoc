import argparse
from collections import deque
from itertools import product
from functools import cache

def get_codes(file_path):
    codes = []
    with open(file_path, 'r') as file:
        for line in file.read().splitlines():
            codes.append(line)
    return codes

def get_keypad(name):
    """
    helper function that returns the keypad according to the given name
    """
    if name == "door":
        return [
            ["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], [None, "0", "A"]
        ]
    elif name == "directional":
        return [
            [None, "^", "A"], ["<", "v", ">"]
        ]
    else:
        return None

def compute_sequences(keypad):
    """
    for a given target_sequence (string) and a keypad (grid), return a list of
      sequences of possible keypad presses made up of (^ v < > A) that
      result in the target_sequence without traveling over the gap in the keypad
    """
    # first, encode the keypad into a map of position coordinates
    pos = {}
    for r in range(len(keypad)):
        for c in range(len(keypad[r])):
            if keypad[r][c] is not None:
                pos[keypad[r][c]] = (r, c)

    # create a map: pair of positions on the keypad --> all sequences that
    #.  can get the robot's funger between two points
    # unless the finger is already at the target (just press A), perform a BFS
    #.  with multiple paths to find the ways to get between the locations
    # since the numeric keypad is small, can be exhaustive about storing the
    #. possibilities
    seqs = {}
    # for each position in the keypad (x) ...
    for x in pos:
        # ... loop through every other target position (y)
        for y in pos:
            if x == y:
                seqs[(x, y)] = ["A"]
                continue
            # BFS
            possibilities = []
            # queue the paths as strings, which will be of increasing length (BFS)
            #. that means we can ignore suboptimal paths once we find a path to the
            #. target that is longer than optimal length
            q = deque([(pos[x], "")])
            optimal = float("inf")
            while q:
                (r, c), moves = q.popleft()
                # 4 directions, with their directional keypad "move"
                for nr, nc, nm in [(r - 1, c, "^"), (r + 1, c, "v"), (r, c - 1, "<"), (r, c + 1, ">")]:
                    if nr < 0 or nc < 0 or nr >= len(keypad) or nc >= len(keypad[0]):
                        continue
                    if keypad[nr][nc] == None:
                        # avoid the gap
                        continue
                    if keypad[nr][nc] == y:
                        # end position -> add to possibilities, not the queue
                        if optimal < len(moves) + 1:
                            break
                        optimal = len(moves) + 1
                        possibilities.append(moves + nm + "A")
                    else:
                        # otherwise, add to the queue
                        q.append(((nr, nc), moves + nm))
                else:
                    continue
                break   # propogate found-it break
            # after BFS:
            # seqs now holds every possible "optimal" combination of moves
            #. to get from x to y
            seqs[(x, y)] = possibilities
    return seqs

# precompute
# declared here because i get an error passing the lengths dict as an argument,
#. even after making sure the keys are still of type tuple.
#.. ideally these would be data members of a class
# all sequences of actions to get between any two places on the door keypad
DOOR_SEQUENCES = compute_sequences(get_keypad("door"))
# all sequences of actions to get between any two places on the directional keypad
DIRECTIONAL_SEQUENCES = compute_sequences(get_keypad("directional"))
# length of shortest possible sequence between each pair on the directional keypad
DIRECTIONAL_LENGTHS = {k: len(v[0]) for k, v in DIRECTIONAL_SEQUENCES.items()}


def solve(target_sequence, seqs, debug):
    # solver needs each move from one position to the next
    #. robot's finger starts over the A key
    target_moves = zip("A" + target_sequence, target_sequence)
    # all optimal sequences of moves for the pairs of target characters
    options = [seqs[(x, y)] for x, y in target_moves]
    cartesian_product_strings = ["".join(x) for x in product(*options)]
    if debug:
        print(options)
        print(cartesian_product_strings)
    return cartesian_product_strings


def PART_ONE(codes, debug=False):

    total = 0
    for target_code in codes:
        print(target_code)
        # instructions for robot at the door
        robot1 = solve(target_code, DOOR_SEQUENCES, debug)
        curr_robot = robot1
        # instructions for subsequent robots
        for _ in range(2):
            possible_instrs = []
            for target in curr_robot:
                possible_instrs += solve(target, DIRECTIONAL_SEQUENCES, debug)
            optimal_len = min(map(len, possible_instrs))
            curr_robot = [seq for seq in possible_instrs if len(seq) == optimal_len]
            debug and print(len(curr_robot[0]))
        # compute complexity
        length = len(curr_robot[0])
        complexity = length * int(target_code[:-1])
        total += complexity
    print(f'total complexity score for {len(codes)} is {total}')


@cache
def compute_length_at_depth(seq, depth=25):
    """
    recursively (DFS, using cache to skip branches)
    compute the length of a sequence to get from x to y, at a depth, where
    depth refers to which robot in the sequence of direction-keypad robots,
    which corresponds to the layer inside the DFS of our tree of possible 
    instruction sequences.
    """
    if depth == 1:
        return sum(DIRECTIONAL_LENGTHS[(x, y)] for x, y in zip("A" + seq, seq))

    length = 0
    for a, b in zip("A" + seq, seq):
        # generator expression to return the best length
        length += min(compute_length_at_depth(subseq, depth-1) for subseq in DIRECTIONAL_SEQUENCES[(a, b)])
    return length
 

def PART_TWO(codes, debug=False):
    total = 0
    debug and print(DIRECTIONAL_LENGTHS)
    for target_code in codes:
        print(target_code)
        # instructions for robot at the door
        robot1 = solve(target_code, DOOR_SEQUENCES, debug)
        length = min(map(compute_length_at_depth, robot1))
        total += length * int(target_code[:-1])
    print(f'total complexity score for {len(codes)} code is {total}')


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="make instructions for series of keypad-typing robots")
    parser.add_argument('file_path', help="path to the text file containing the needed codes")
    args = parser.parse_args()
    codes = get_codes(args.file_path)
    PART_ONE(codes, False)
    print()
    PART_TWO(codes, False)