import argparse
import re
import math

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

def minimize_cost_brute(problem, button_max):
    """
    finds the minimum cost to reach the prize location exactly
    button_max is the maximum number of button presses to be attempted
    rather a brute-force approach, exploiting the fact that the destination must be reached in exactly
    """
    button_a = problem['Button A']
    button_b = problem['Button B']
    prize = problem['Prize']
    
    target_x = prize['X']
    target_y = prize['Y']

    ax, ay = button_a['X'], button_a['Y']
    bx, by = button_b['X'], button_b['Y']

    cost_a = 3
    cost_b = 1

    min_cost = float('inf')
    best_a_presses = 0
    best_b_presses = 0

    # iterate over possible counts for A presses
    end_a = min(button_max, target_x // ax + 1)
    for a_presses in range(end_a):
        remaining_x = target_x - (a_presses * ax)
        remaining_y = target_y - (a_presses * ay)

        # check if the remaining prize location can be exactly by pressing B
        if remaining_x >= 0 and remaining_y >= 0 and remaining_x % bx == 0 and remaining_y % by == 0:
            # match X
            b_presses = remaining_x // bx
            # match Y
            if (b_presses <= button_max) and (b_presses * by == remaining_y):
                # calculate total cost and compare
                cost = cost_a * a_presses + cost_b * b_presses
                if cost < min_cost:
                    min_cost = cost
                    best_a_presses = a_presses
                    best_b_presses = b_presses

    return {
        'Cost': min_cost,
        'A': best_a_presses,
        'B': best_b_presses
    }


def PART_ONE(problems, debug=False):

    total_min = 0
    for idx, problem in enumerate(problems, 1):
        ans = minimize_cost_brute(problem, 100)
        min_cost = ans['Cost']
        if math.isfinite(min_cost):
            total_min += min_cost
        if debug:
            a = ans['A']
            b = ans['B']
            x = problem['Prize']['X']
            y = problem['Prize']['Y']
            print(f'Problem {idx}: X={x}, Y={y}, cost={min_cost}, A presses={a}, B presses={b}')
    print(f'Total cost after {len(problems)} claw machine problems is {total_min}')

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Optimize claw-machine movements defined in text.")
    parser.add_argument('file_path', help="Path to the text file containing claw-machine problems.")
    args = parser.parse_args()
    problems = parse_optimization_file(args.file_path)

    PART_ONE(problems, True)
    print()
    # PART_TWO(grid, False)