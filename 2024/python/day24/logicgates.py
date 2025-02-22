import argparse

def get_input(file_path):
    known_values = {}   # x00: 1 stored as: x00 --> 1
    formulae = {}       # x00 AND y00 -> z00 stored as:  z00 --> (AND, x00, y00)
    with open(file_path, 'r') as file:
        for line in file:
            if line.isspace():
                break
            x, y = line.split(': ')
            known_values[x] = int(y)
        for line in file:
            x, op, y, z = line.replace(' -> ', ' ').split()
            formulae[z] = (op, x, y)
    return known_values, formulae

OPERATORS = {
    'OR': lambda x, y: x | y,
    'AND': lambda x, y: x & y,
    'XOR': lambda x, y: x ^ y
}

def calc(knowns, formulae, wire):
    """
    recursive function that calculates the value on a given wire
    add results to the knowns[] parameter to redue recursion calls
    """
    if wire in knowns:
        return knowns[wire]
    op, x, y = formulae[wire]
    knowns[wire] = OPERATORS[op](calc(knowns, formulae, x), calc(knowns, formulae, y))
    return knowns[wire]


def PART_ONE(knowns, formulae, debug=False):
    if debug:
        print(knowns)
        print(formulae)
    
    # calculate the z-output values, starting with z00 and checking whether that z-wire exists
    ii, z_values = 0, []
    while True:
        key = 'z' + str(ii).rjust(2, '0')
        if key not in formulae:
            break
        z_values.append(calc(knowns, formulae, key))
        ii += 1
    debug and print(z_values)

    # reverse the z-values (z00 on the right end), convert into a binary number
    binary = "".join(map(str, z_values[::-1]))
    ans = int(binary, 2)
    print(f'number represented by the z-wires is {ans}')
    

def PART_TWO(knowns, formulae, debug=False):
    ...

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="compute logic gate array output")
    parser.add_argument('file_path', help="path to the text file containing the gates and initial values")
    args = parser.parse_args()
    knowns, formulae = get_input(args.file_path)
    PART_ONE(knowns, formulae, False)
    print()
    PART_TWO(knowns, formulae, True)