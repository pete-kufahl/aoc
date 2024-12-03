import sys

def validate_levels(levels, lo, hi) -> bool:
    """
    check differences against range and monotonicity in a single pass through
    the numbers list (levels)
    """
    increasing = None  # determine the direction during the first comparison

    for i in range(1, len(levels)):
        diff = levels[i] - levels[i - 1]
        
        # difference versus bounds
        if abs(diff) < lo or abs(diff) > hi:
            return False
        
        # determine/validate monotonicity
        if increasing is None:
            if diff != 0:
                increasing = diff > 0
        else:
            if (increasing and diff < 0) or (not increasing and diff > 0):
                return False
            
    return True


if __name__ == "__main__":

    file_name = "input.txt"
    if len(sys.argv) > 1:
        file_name = sys.argv[1]

    try:
        safe_lines = 0
        with open(file_name, 'r') as file:
            for i, line in enumerate(file):
                rule1, rule2 = False, False
                levels = []

                parts = line.split()    # handles multiple whitespaces
                for part in parts:
                    if part.isdigit():
                        levels.append(int(part))
                if len(levels) > 1:
                    if validate_levels(levels, lo=1, hi=3):
                        safe_lines += 1
                else:
                    print(f'insufficient data found in line {i}: {line}')
                    continue

        print (f'{safe_lines} safe lines of numbers')
    except FileNotFoundError:
        print(f"The file {file_name} was not found.")
    except IOError:
        print("An error occurred while reading the file.")
