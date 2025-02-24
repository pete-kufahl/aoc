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
    """
    evaluate the output of a logic circuit, given a set of initial known values
    and set of logical operations between wires
    """
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
    

def printwire(wire, formulae, depth=0):
    F = formulae
    if wire[0] in "xy":
        return "  " * depth + wire
    op, x, y = formulae[wire]
    return "  " * depth + op + " (" + wire + ")\n" + printwire(x, F, depth+1) + "\n" + printwire(y, F, depth+1)


def verify_intermediate_xor(wire, num, formulae):
    if wire not in formulae:
        return False
    op, x, y = formulae[wire]
    if op != "XOR":
        return False
    return verify_operands(num, x, y)


def verify_direct_carry(wire, num, formulae):
    if wire not in formulae:
        return False
    op, x, y = formulae[wire]
    if op != "AND":
        return False
    return verify_operands(num, x, y)


def verify_operands(num, x, y):
    x_wire = 'x' + str(num).rjust(2, "0")
    y_wire = 'y' + str(num).rjust(2, "0")
    return sorted([x, y]) == [x_wire, y_wire]


def verify_recarry(wire, num, formulae):
    if wire not in formulae:
        return False
    op, x, y = formulae[wire]
    if op != "AND":
        return False
    return (verify_intermediate_xor(x, num, formulae) and verify_carry_bit(y, num, formulae)) or\
        (verify_intermediate_xor(y, num, formulae) and verify_carry_bit(x, num, formulae))


def verify_carry_bit(wire, num, formulae):
    if wire not in formulae:
        return False
    op, x, y = formulae[wire]
    if num == 1:
        return op == "AND" and verify_operands(0, x, y)
    if op != "OR":
        return False
    return (verify_direct_carry(x, num - 1, formulae) and verify_recarry(y, num - 1, formulae)) or\
        (verify_direct_carry(y, num - 1, formulae) and verify_recarry(x, num - 1, formulae))


def verify_z(wire, num, formulae):
    if wire not in formulae:
        return False
    op, x, y = formulae[wire]
    if op != "XOR":
        return False
    if num == 0:
        return verify_operands(0, x, y)
    # and-statments start with non-recursive function
    return (verify_intermediate_xor(x, num, formulae) and verify_carry_bit(y, num, formulae)) or\
        (verify_intermediate_xor(y, num, formulae) and verify_carry_bit(x, num, formulae))


def verify(num, formulae):
    z_wire = 'z' + str(num).rjust(2, "0")
    return verify_z(z_wire, num, formulae)


def find_progress(formulae, debug):
    level = 0
    while True:
        debug and print('----')
        if not verify(level, formulae): break
        level += 1
    return level
    

def PART_TWO(formulae, debug=False):
    """
    given a set of formulae, including those for x-wires, y-wires, and z-wires, figure out
    which 8 gates have their wires swapped in order to make the entire system add any
    x-number to any y-number to make the correct z-number
    """
    gates = []
    level = find_progress(formulae, debug)
    print(f'made it to level {level}')
    
    for _ in range(4):
        baseline = find_progress(formulae, debug)
        for x in formulae:
            for y in formulae:
                if x == y:
                    continue
                formulae[x], formulae[y] = formulae[y], formulae[x]
                if find_progress(formulae, debug) > baseline:
                    break
                formulae[x], formulae[y] = formulae[y], formulae[x] # swap back
            else:
                continue
            break
        print(x, y)
        gates += [x, y]

    print(",".join(sorted(gates)))

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="compute logic gate array output")
    parser.add_argument('file_path', help="path to the text file containing the gates and initial values")
    args = parser.parse_args()
    knowns, formulae = get_input(args.file_path)
    PART_ONE(knowns, formulae, False)
    print()
    PART_TWO(formulae, False)