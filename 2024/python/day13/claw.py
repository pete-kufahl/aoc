import argparse
import re

def parse_optimization_file(file_path):
    """
    parse a file of three-line problems into list of dict
    """
    problems = []
    current_problem = []

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                current_problem.append(line)
            else:
                # blank line indicates the end of a problem; ensure it's three lines
                if len(current_problem) == 3:
                    problems.append(parse_problem(current_problem))
                current_problem = []    

    # add the last problem if the file doesn't end with a blank line
    if len(current_problem) == 3:
        problems.append(parse_problem(current_problem))

    return problems


def parse_problem(lines):
    """
    parse a three-line problem into a dictionary
    """
    button_a = {}
    if match := re.search(r'Button A: X\+(\d+), Y\+(\d+)', lines[0]):
        button_a['X'] = int(match.group(1))
        button_a['Y'] = int(match.group(2))

    button_b = {}
    if match := re.search(r'Button B: X\+(\d+), Y\+(\d+)', lines[1]):
        button_b['X'] = int(match.group(1))
        button_b['Y'] = int(match.group(2))

    prize = {}
    if match := re.search(r'Prize: X=(\d+), Y=(\d+)', lines[2]):
        prize['X'] = int(match.group(1))
        prize['Y'] = int(match.group(2))

    return {
        'Button A': button_a,
        'Button B': button_b,
        'Prize': prize
    }

def PART_ONE(problems, debug=False):
    if debug:
        for idx, problem in enumerate(problems, 1):
            print(f"Problem {idx}:")
            print(f"  Button A: X+{problem['Button A']['X']}, Y+{problem['Button A']['Y']}")
            print(f"  Button B: X+{problem['Button B']['X']}, Y+{problem['Button B']['Y']}")
            print(f"  Prize: X={problem['Prize']['X']}, Y={problem['Prize']['Y']}")

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Optimize claw-machine movements defined in text.")
    parser.add_argument('file_path', help="Path to the text file containing claw-machine problems.")
    args = parser.parse_args()
    problems = parse_optimization_file(args.file_path)

    PART_ONE(problems, True)
    print()
    # PART_TWO(grid, False)