import re

def process_3_patterns(file_path):

    mul_pattern = re.compile(r"mul\((-?\d+),(-?\d+)\)")
    do_pattern = re.compile(r"do\(\)")
    dont_pattern = re.compile(r"don't\(\)")

    with open(file_path, 'r') as file:
        content = file.read()  # Read the entire file content

    do_matches = list(do_pattern.finditer(content))
    dont_matches = list(dont_pattern.finditer(content))
    mul_matches = list(mul_pattern.finditer(content))
    
    # Combine and sort do() and don't() matches by position
    states = [
        (match.start(), "enable") for match in do_matches
    ] + [
        (match.start(), "disable") for match in dont_matches
    ]
    states.sort(key=lambda x: x[0])

    current_state = "enable"
    sum_products = 0
    
    # process mul(X, Y) matches based on the most recent state
    for match in mul_matches:
        start = match.start()
        # update current state if needed
        while len(states) > 0 and start > states[0][0]:
            current_state = states.pop(0)[1]
            print(f'at position {start}, state updated to {current_state}')

        if current_state == "enable":
            x, y = match.groups()
            print(f"At position {start}: X = {x}, Y = {y}")
            sum_products += int(x) * int(y)
        else:
            print('skipped ...')

    return sum_products

if __name__ == '__main__':

    file_path = 'input.txt' 
    ans = process_3_patterns(file_path)
    print(f'sum of products is: {ans}')
