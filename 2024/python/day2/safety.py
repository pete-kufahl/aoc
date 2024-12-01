import sys

def monotonic_levels(levels) -> bool:
    increasing = False
    for i in range(1, len(levels)):
        if i == 1:
            increasing = levels[i] > levels[i-1]
        else:
            if increasing and levels[i] <= levels[i-1]:
                return False
            if (not increasing) and levels[i] >= levels[i-1]:
                return False 
    return True

def safe_differences(levels, lo, hi) -> bool:
    for i in range(1, len(levels)):
        diff = abs(levels[i] - levels[i-1])
        if diff < lo or diff > hi:
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
                    rule1 = monotonic_levels(levels)
                    rule2 = rule1 and safe_differences(levels, lo=1, hi=3)
                    if rule2:
                        safe_lines += 1
                else:
                    print(f'insufficient data found in line {i}: {line}')
                    continue

        print (f'{safe_lines} safe lines of numbers')
    except FileNotFoundError:
        print(f"The file {file_name} was not found.")
    except IOError:
        print("An error occurred while reading the file.")
