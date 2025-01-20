import argparse
import re


def read_file(file_path):
    """
    read input file; everything that matters is a number
    """
    with open(file_path, 'r') as file:
        a, b, c, *program = map(int, re.findall(r"\d+", file.read()))
    return [a, b, c], program

def run_program(a, b, c, instructions):
    pass

def PART_ONE(registers, instructions, debug):
    """
    run the program
    """
    run_program(*registers, instructions)


def PART_TWO(registers, instructions, debug):
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="predict activity of 3-bit computer")
    parser.add_argument('file_path', help="path to the text file containing registers and instructions")
    args = parser.parse_args()
    
    registers, instructions = read_file(args.file_path)
    print(registers)
    print(instructions)

    PART_ONE(registers, instructions, debug=False)
    print()
