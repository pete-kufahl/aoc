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
    end_a = min(int(button_max), target_x // ax + 1)
    print(f'iterating A, 0 to {end_a} ....')
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

def compute_cost_lineqs(problem, max_presses=float('inf')):
    """
    instead of looping, observe that the problem of:
      A * dist_ax * x + B * dist_bx * x = prize_x
      A * dist_ay * y + B * dist_by * y = prize_y
    is a system of 2 linear equations with 2 unknowns (A, B)
      and therefore has one unique solution.
    so, the problem of minimizing the cost is a trick question.
    calculate the cost of the solution, provided that A < button_max and B < button_max
    """
    button_a = problem['Button A']
    button_b = problem['Button B']
    prize = problem['Prize']

    ax, ay = button_a['X'], button_a['Y']
    bx, by = button_b['X'], button_b['Y']
    px, py = prize['X'], prize['Y']

    cost_a = 3
    cost_b = 1

    """
        1. start here -> rename coeffs
        A * dist_ax * x + B * dist_bx * x = prize_x   --> Ax * A + Bx * B = Px
        A * dist_ay * y + B * dist_by * y = prize_y   --> Ay * A + By * B = Py

        2. multiply top eq by By, bottom eq by Bx
        Ax * By * A + Bx * By * B = By * Px
        Ay * Bx * A + Bx * By * B = Bx * Py

        3. subtract bottom from top, second term on left cancels
        (Ax * By - Ay * Bx) * A = By * Px - Bx * Px

        4. solve for A, substitute into Ax * A + Bx * B = Px
    """
    # step 4
    if (ax * by - ay * bx) == 0:
        return { 'Cost': float('inf'), 'A': 0, 'B': 0 }
    
    a_presses = (by * px - bx * py) / (ax * by - ay * bx)
    b_presses = (px - ax * a_presses) / bx

    if a_presses < max_presses and b_presses < max_presses:
        # maybe allow for a little roundoff?
        precision = 0.0000001
        if a_presses % 1 < precision and b_presses % 1 < precision:
            cost = round(a_presses) * cost_a + round(b_presses) * cost_b
        else:
            cost = float('inf')
    else:
        cost = float('inf')

    return {
        'Cost': cost,
        'A': a_presses,
        'B': b_presses
    }



def PART_ONE(problems, debug=False):
    total_min = 0
    for idx, problem in enumerate(problems, 1):
        ans = compute_cost_lineqs(problem, 100)
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

def PART_TWO(problems, debug=False):
    total_min = 0
    for idx, problem in enumerate(problems, 1):
        problem['Prize']['X'] = 10000000000000 + problem['Prize']['X']
        problem['Prize']['Y'] = 10000000000000 + problem['Prize']['Y']
        ans = compute_cost_lineqs(problem)
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

    PART_ONE(problems, False)
    print()
    PART_TWO(problems, False)