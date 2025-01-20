import argparse
import re


def read_file(file_path):
    """
    read input file; everything that matters is a number
    """
    with open(file_path, 'r') as file:
        a, b, c, *program = map(int, re.findall(r"\d+", file.read()))
    return [a, b, c], program


def combo(operand, a, b, c):
    if 0 <= operand <= 3:
        return operand
    if operand == 4:
        return a
    if operand == 5:
        return b
    if operand == 6:
        return c
    else:
        raise RuntimeError(f'unrecognized operand combination {operand}')
    

def run_program(registers, instructions, debug=False, expected=[]):
    debug2 = False
    a, b, c = registers
    orig_a = a
    result = []
    i = 0
    while i < len(instructions) - 1:
        inc2 = True
        instr = instructions[i]
        operand = instructions[i+1]
        debug2 and print(instr, operand)
        if instr == 0:      # ADV
            a = a >> combo(operand, a, b, c)
            debug and print(f'a = {a}')
        if instr == 1:      # BXL
            b = b ^ operand
            debug2 and print(f'b = {b}')
        if instr == 2:      # BST
            b = combo(operand, a, b, c) % 8
            debug2 and print(f'b = {b}')
        if instr == 3:      # JNZ
            if a != 0:
                i = operand
                inc2 = False
        if instr == 4:      # BXC
            b = b ^ c
            debug2 and print(f'b = {b}')
        if instr == 5:      # OUT
            result.append(combo(operand, a, b, c) % 8)
            if debug:
                # print(f'result = ', result)
                if len(result) == len(expected):
                    match = True
                    for x, y in zip(result, expected):
                        if x != y:
                            match = False
                    if match:
                        print(f'they match! {result}')
                        return result, orig_a
                    else:
                        print(f'result={result}, expected={expected}')
                        return result, -1
        if instr == 6:      # BDV
            b = a >> combo(operand, a, b, c)
            debug2 and print(f'b = {b}')
        if instr == 7:      # CDV
            c = a >> combo(operand, a, b, c)
            debug2 and print(f'c = {c}')
        if inc2:
            i += 2
    return result, orig_a

def PART_ONE(registers, instructions, debug):
    """
    run the program
    """
    ans, _ = run_program(registers, instructions)
    print(*ans, sep=",")


def PART_TWO_RECURSIVE(program):
    """
    registers B, C are initially 0, so we don't need that param
    solution is from HyperNeutrino, simplified with baked-n assumptions
    """
    def find(target, ans):
        if target == []: return ans
        for t in range(8):
            a = ans << 3 | t
            b, c = 0, 0
            output = None

            def combo(operand):
                if 0 <= operand <= 3:
                    return operand
                return {4: a, 5: b, 6: c}.get(operand, RuntimeError('unknown operand'))

            for ptr in range(0, len(program)-2, 2):
                ins, operand = program[ptr], program[ptr+1]
                if ins == 1:
                    b = b ^ operand
                elif ins == 2:
                    b = combo(operand) % 8
                elif ins == 4:
                    b = b ^ c
                elif ins == 5:
                    output = combo(operand) % 8
                elif ins == 6:
                    b = a >> combo(operand)
                elif ins == 7:
                    c = a >> combo(operand)
                if output == target[-1]:
                    sub = find(target[:-1], a)
                    if sub is None: continue
                    return sub
                
    print(find(program, 0))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="predict activity of 3-bit computer")
    parser.add_argument('file_path', help="path to the text file containing registers and instructions")
    args = parser.parse_args()
    
    registers, instructions = read_file(args.file_path)

    # PART_ONE(registers, instructions, debug=False)
    PART_TWO_RECURSIVE(instructions)
