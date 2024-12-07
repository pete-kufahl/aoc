
from itertools import product
import argparse

def test_add_mult(test_value, operands):
    """
    blunt-force approach to finding if a linear (* and + operations) combination
     of the operands can produce test_value.
    if n = number of operands,
    O(n) each combination * O(2^(n-1)) combinations = O(n * 2^(n-1))
    """
    n = len(operands)
    if n == 1:
        return operands[0] == test_value

    # functional language-inspired tools to generate all operator combinations
    for ops in product(['+', '*'], repeat=n-1):
        # build and evaluate the expression
        result = operands[0]
        for i in range(n-1):
            if ops[i] == '+':
                result += operands[i+1]
            elif ops[i] == '*':
                result *= operands[i+1]

        if result == test_value:
            return True

    return False

def test_add_mult_concat(test_value, operands):
    """
    blunt-force approach to finding if any combination by *, + or ||
     of the operands can produce test_value.
    with || being a concatenation of the digits
    if n = number of operands,
    O(n) each combination * O(3^(n-1)) combinations = O(n * 3^(n-1))
    """
    n = len(operands)
    if n == 1:
        return operands[0] == test_value

    # functional language-inspired tools to generate all operator combinations
    for ops in product(['+', '*', '||'], repeat=n-1):
        # build and evaluate the expression
        result = operands[0]
        for i in range(n-1):
            if ops[i] == '+':
                result += operands[i+1]
            elif ops[i] == '*':
                result *= operands[i+1]
            elif ops[i] == '||':
                result = int(str(result) + str(operands[i+1]))

        if result == test_value:
            return True

    return False

if __name__ == '__main__':
    debug = False
    parser = argparse.ArgumentParser(description="Find the traversal path of a text maze.")
    parser.add_argument('file_path', help="Path to the text file containing the maze.")
    args = parser.parse_args()

    total_calibration_value1, total_calibration_value2 = 0, 0
    line_count = 0
    with open(args.file_path, 'r') as file:
        for line in file:
            # Parse each line
            line = line.strip()
            if not line:
                continue
            try:
                # Split into solution and operands
                test_value, operands_str = line.split(':')
                test_value = int(test_value.strip())
                operands = list(map(int, operands_str.strip().split()))

                # Check if the solution is possible
                line_count += 1
                ans1 = test_add_mult(test_value, operands)
                if ans1:
                    total_calibration_value1 += test_value
                ans2 = test_add_mult_concat(test_value, operands)
                if ans2:
                    total_calibration_value2 += test_value

            except ValueError:
                print(f"Error parsing line: {line}")
                continue
    print (f'after {line_count} combinations, total calibration value (+, *) is {total_calibration_value1}')
    print (f'after {line_count} combinations, total calibration value (+, *, ||) is {total_calibration_value2}')
